# Library
import psycopg2
import pandas as pd
from sqlalchemy import create_engine, text

# Define the database connection parameters
db_params = {
    'host': 'dfdsfsdfsdfds',
    'database': 'dfsdfdsfdsfds',
    'user': 'dfdsfsdfsdfsd',
    'password': 'dfdsfdsfsdfds'
}

engine = create_engine(f'postgresql://{db_params["user"]}:{db_params["password"]}@{db_params["host"]}:5432/{db_params["database"]}')

df = pd.read_csv(r'C:\Users\rjakkula\Documents\DE\visualstudio\PythonSQL\Data\CRODChildCareIntercepts1-1topresent.csv')
table_name ='cdor_taxintercept_20240321'
df.to_sql(table_name, engine, schema='lower_backup', if_exists='replace', index=False)
