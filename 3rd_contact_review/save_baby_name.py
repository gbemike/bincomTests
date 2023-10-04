import pandas as pd
import psycopg2
from sqlalchemy import create_engine
from decouple import config
from io import StringIO

conn = psycopg2.connect(
    host=config("DB_HOST"),
    database=config("DB_NAME"),
    user=config("DB_USER"),
    password=config("DB_PASSWORD")
)

cur = conn.cursor()

sql = """ CREATE TABLE BABY (
rank SERIAL PRIMARY_KEY,
male_name VARCHAR(255),
female_name VARCHAR(255)
) """

cur.execute(sql)

# Commit the changes to the database
conn.commit()

df = pd.read_csv('babynames.csv')

# Create a string buffer and write the CSV data to it
csv_data = StringIO(df)

cur.copy_from(csv_data, 'baby', sep=',', columns=('rank', 'male_name', 'female_name'))

conn.commit()

# Close the cursor and database connection
cur.close()
conn.close()

