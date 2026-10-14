import pandas as pd

def clean_orders(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # 1. Duplicates: the same order_id should only appear once
    df = df.drop_duplicates(subset="order_id")

    # 2. Inconsistent text: " dallas " and "Dallas" are the same city
    df["city"] = df["city"].str.strip().str.title()

    # 3. Bad dates: convert to a real datetime type
    df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")
    df = df.dropna(subset=["order_date"])        # an order with no date is unusable

    # 4. Invalid quantities: missing or <= 0 can't be real orders
    df = df[df["quantity"].notna() & (df["quantity"] > 0)]
    df["quantity"] = df["quantity"].astype(int)

    return df.reset_index(drop=True)