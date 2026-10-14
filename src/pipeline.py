import logging
from extract import extract_orders, extract_products
from transform import clean_orders
from load import load_to_db

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s %(levelname)s %(message)s")
log = logging.getLogger(__name__)

def run():
    try:
        orders = extract_orders()
        products = extract_products()
        log.info("Extracted %d orders", len(orders))

        clean = clean_orders(orders)
        log.info("Kept %d rows, dropped %d", len(clean), len(orders) - len(clean))

        load_to_db(clean, "orders")
        load_to_db(products, "products")
        log.info("Pipeline finished successfully")
    except Exception:
        log.exception("Pipeline failed")
        raise

if __name__ == "__main__":
    run()