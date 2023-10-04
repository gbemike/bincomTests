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

# Execute a query
'''cur.execute("""CREATE TABLE test (
            id serial PRIMARY KEY, 
            num integer, 
            data VARCHAR);""")'''

query = "INSERT INTO test (num, data) VALUES (%s, %s)"
records = [
    (300, "gbemideimoleayo"),
    (200, "tunmikeandYanmike")
    ]

for i in records:
    cur.execute(query, i)

conn.commit()

cur.close()
conn.close()