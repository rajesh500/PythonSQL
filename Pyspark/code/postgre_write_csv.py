# Library
import psycopg2
import pandas as pd
from sqlalchemy import create_engine, text

# Define the database connection parameters
db_params = {
    'host': 'sdfsdfsdfsdf',
    'database': 'sdfsdfsdfdsf',
    'user': 'dsfsdfdsfdsf',
    'password': 'dfsdfsdfsdfsd'
}

engine = create_engine(f'postgresql://{db_params["user"]}:{db_params["password"]}@{db_params["host"]}:5432/{db_params["database"]}')

df = pd.read_csv(r'C:\Users\rjakkula\Documents\DE2\Data\Tax Intercept Removed Records 2024 Requiring RefundData2.csv')
table_name ='table'
df.to_sql(table_name, engine, schema='schema', if_exists='replace', index=False)
