# Library
import psycopg2
import pandas as pd
from sqlalchemy import create_engine, text

# Define the database connection parameters
db_params = {
    'host': 'dasdsdfsdfds',
    'database': 'fsdfsdfdsfds',
    'user': 'fsdfdsfdsff',
    'password': 'sdfsdfdsfdfsdf'
}

engine = create_engine(f'postgresql://{db_params["user"]}:{db_params["password"]}@{db_params["host"]}:5432/{db_params["database"]}')

df = pd.read_csv(r'C:\Users\rjakkula\Downloads\file.csv')
table_name ='table'
df.to_sql(table_name, engine, schema='lower', if_exists='replace', index=False)
