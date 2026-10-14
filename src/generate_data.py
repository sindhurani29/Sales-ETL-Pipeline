import random
import pandas as pd
from datetime import date, timedelta

random.seed(42)

products = pd.DataFrame({
    "product_id": ["P001", "P002", "P003", "P004"],
    "product_name": ["Laptop", "Headphones", "Desk Chair", "Monitor"],
    "category": ["Electronics", "Electronics", "Furniture", "Electronics"],
    "unit_price": [800, 60, 150, 220],
})
products.to_csv("data/raw/products.csv", index=False)

cities = ["Dallas", "dallas ", "AUSTIN", "Austin", " Houston", "houston"]
rows = []
for i in range(1, 501):
    rows.append({
        "order_id": i,
        "customer_id": f"C{random.randint(1, 80):03d}",
        "product_id": random.choice(products["product_id"]),
        "quantity": random.choice([1, 2, 3, 4, None, -1]),   # missing and invalid values
        "order_date": (date(2026, 1, 1) + timedelta(days=random.randint(0, 200))).isoformat()
                      if random.random() > 0.03 else None,   # some missing dates
        "city": random.choice(cities),                       # inconsistent text
    })

df = pd.DataFrame(rows)
df = pd.concat([df, df.sample(15, random_state=1)])          # add duplicate rows
df.to_csv("data/raw/orders.csv", index=False)
print("Generated", len(df), "rows")