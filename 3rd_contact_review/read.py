import pandas as pd
import psycopg2
from sqlalchemy import create_engine
from decouple import config

conn= psycopg2.connect(
    host=config("DB_HOST"),
    database=config("DB_NAME"),
    user=config("DB_USER"),
    password=config("DB_PASSWORD")
)

# Open a cursor to perform database operations
cur = conn.cursor()

get_table = cur.execute("SELECT * FROM test")

all_records = cur.fetchall()
for i in all_records:
    print(i)