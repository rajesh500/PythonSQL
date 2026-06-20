# Library
import psycopg2
import pandas as pd
from sqlalchemy import create_engine, text

# Define the database connection parameters
db_params = {
    'host': 'fsdfdsfdsfdsfsdf',
    'database': 'sdfsdfsdfds',
    'user': 'dsfsdfdsfds',
    'password': 'fsdfdsfsdfdsfds'
}

engine = create_engine(f'postgresql://{db_params["user"]}:{db_params["password"]}@{db_params["host"]}:5432/{db_params["database"]}')

df = pd.read_csv(r'C:\Users\rjakkula\Documents\DE\visualstudio\PythonSQL\Data\Book2.csv')
table_name ='chats_tb1_second'
df.to_sql(table_name, engine, schema='lower_backup', if_exists='replace', index=False)
