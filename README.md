# Sales ETL Pipeline

A pipeline that cleans messy sales CSV data and loads it into SQLite for analysis.

## Tech
Python, pandas, SQLite, pytest (pandas, data cleaning, ETL, SQLite, SQL (GROUP BY, JOIN, HAVING), logging, testing, and scheduling.)

## How to run
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python src/generate_data.py
python src/pipeline.py

## Project structure
- src/ : extract, transform, load, pipeline code
- sql/ : analysis queries
- tests/ : unit tests
- data/raw/ : input CSVs

## What I learned
(Your own notes: cleaning, idempotency, logging, SQL joins)

### Notes
Why is extract a separate function from transform?
What does idempotent mean, and which line of code makes our load idempotent?
When do you use HAVING instead of WHERE?
Why did we convert order_date to a real date type before the monthly query?