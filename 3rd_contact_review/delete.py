import pandas as pd
import psycopg2
from sqlalchemy import create_engine
from decouple import config

conn = psycopg2.connect(
    host=config("DB_HOST"),
    database=config("DB_NAME"),
    user=config("DB_USER"),
    password=config("DB_PASSWORD")
)
 
cur = conn.cursor()
query_statement = """ DELETE FROM test WHERE num = %s  """
cur.execute(query_statement, [200])
conn.commit()
print("Deleted Successfully")