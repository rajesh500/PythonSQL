# Library
import psycopg2
import pandas as pd
from sqlalchemy import create_engine, text
import csv 

# Define the database connection parameters
db_params = {
    'host': 'sdfsdfdsfdsfdsfds',
    'database': 'fvdfsdfdsfds',
    'user': 'sdfdsfdsfdsf',
    'password': 'dfdsfsdfsdfsdf'
}

engine = create_engine(f'postgresql://{db_params["user"]}:{db_params["password"]}@{db_params["host"]}:5432/{db_params["database"]}')

rdf = pd.read_sql_table('t_auth_encmbr_20230719', engine, schema='lower_backup')
print(rdf.columns)

#column_names = ['Name', 'Age', 'Height']
column_names = rdf.columns
rdf.to_csv(r'C:\Users\rjakkula\Documents\DE\visualstudio\PythonSQL\postgres_table_data_csv2.csv', header=column_names)

