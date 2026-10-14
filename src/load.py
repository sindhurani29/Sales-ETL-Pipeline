import sqlite3
from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parent.parent

def load_to_db(df: pd.DataFrame, table: str, db_path=PROJECT_ROOT / "sales.db"):
    with sqlite3.connect(db_path) as conn:
        df.to_sql(table, conn, if_exists="replace", index=False)