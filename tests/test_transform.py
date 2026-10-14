import pandas as pd
from src.transform import clean_orders

def test_clean_orders_removes_bad_rows():
    raw = pd.DataFrame({
        "order_id": [1, 1, 2, 3],
        "customer_id": ["C1", "C1", "C2", "C3"],
        "product_id": ["P001"] * 4,
        "quantity": [2, 2, -1, 3],
        "order_date": ["2026-01-01", "2026-01-01", "2026-01-02", None],
        "city": [" dallas", " dallas", "Austin", "Houston"],
    })
    result = clean_orders(raw)
    assert len(result) == 1                 # dupes, negative qty, null date removed
    assert result.loc[0, "city"] == "Dallas"

    Run it with python -m pytest from the project root (create an empty src/__init__.py if imports fail).