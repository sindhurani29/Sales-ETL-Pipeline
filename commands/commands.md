### Run the commands in python shell
Explore the data before cleaning it. Profile the data before touching it to find out what’s broken.

from src.extract import extract_orders
df = extract_orders()
df.info()                    # column types and null counts
df.isna().sum()              # where are the nulls?
df.duplicated().sum()        # how many duplicate rows?
df["city"].value_counts()    # spot inconsistent text

----------------------
Final check
python src/pipeline.py

cross check
from src.extract import extract_orders
df = extract_orders()
print("duplicates:", df.duplicated(subset="order_id").sum())
print("missing qty:", df["quantity"].isna().sum())
print("negative qty:", (df["quantity"] < 0).sum())
print("missing date:", df["order_date"].isna().sum())
exit()

Run sql
sqlite3 -header -column sales.db < sql/analysis.sql

### Notes
- Why is extract a separate function from transform?
- What does idempotent mean, and which line of code makes our load idempotent?
- When do you use HAVING instead of WHERE?
- Why did we convert order_date to a real date type before the monthly query?