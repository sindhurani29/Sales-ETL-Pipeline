-- Scenario 1: “Which city sells the most?” (GROUP BY and aggregation)
SELECT city, COUNT(*) AS num_orders, SUM(quantity) AS units_sold
FROM orders
GROUP BY city
ORDER BY units_sold DESC;

-- Scenario 2: “What’s our revenue per product?” (JOIN)
SELECT p.product_name, SUM(o.quantity * p.unit_price) AS revenue
FROM orders o
JOIN products p ON o.product_id = p.product_id
GROUP BY p.product_name
ORDER BY revenue DESC;

-- Scenario 3: “How is revenue trending monthly?” (date functions)
SELECT strftime('%Y-%m', o.order_date) AS month,
       SUM(o.quantity * p.unit_price) AS revenue
FROM orders o
JOIN products p ON o.product_id = p.product_id
GROUP BY month
ORDER BY month;

-- Scenario 4: “Who are our loyal customers?” (HAVING)
SELECT customer_id, COUNT(*) AS num_orders
FROM orders
GROUP BY customer_id
HAVING COUNT(*) >= 8
ORDER BY num_orders DESC;

-- Scenario 5: “Do any orders reference a product that doesn’t exist?” (data validation with LEFT JOIN)
SELECT o.order_id, o.product_id
FROM orders o
LEFT JOIN products p ON o.product_id = p.product_id
WHERE p.product_id IS NULL;





