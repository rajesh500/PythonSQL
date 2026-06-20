# Library
import psycopg2
import pandas as pd
from sqlalchemy import create_engine, text

# Define the database connection parameters
db_params = {
    'host': 'ssdsfdfsdfsd',
    'database': 'sdfsdfdsf',
    'user': 'sdfsdfsdfds',
    'password': 'sdfsdfsdfds'
}

engine = create_engine(f'postgresql://{db_params["user"]}:{db_params["password"]}@{db_params["host"]}:5432/{db_params["database"]}')

rdf = pd.read_sql_table('employee', engine, schema='schema')
print(rdf)