from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parent.parent
RAW_DIR = PROJECT_ROOT / "data" / "raw"

def extract_orders(path=RAW_DIR / "orders.csv"):
    return pd.read_csv(path)

def extract_products(path=RAW_DIR / "products.csv"):
    return pd.read_csv(path)