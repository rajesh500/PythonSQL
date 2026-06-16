# Library
import psycopg2
import pandas as pd
from sqlalchemy import create_engine, text
import csv 

# Define the database connection parameters
db_params = {
    'host': 'ec2-34-206-124-133.compute-1.amazonaws.com',
    'database': 'db5g29u2cel02j',
    'user': 'u61gjpmvjt5prl',
    'password': 'p6a67b3b89c0babe7005c17bd8e2af98551fcbdde9aae7f26fd80d45ad0d73024'
}

engine = create_engine(f'postgresql://{db_params["user"]}:{db_params["password"]}@{db_params["host"]}:5432/{db_params["database"]}')

rdf = pd.read_sql_table('t_auth_encmbr_20230719', engine, schema='lower_backup')
print(rdf.columns)

#column_names = ['Name', 'Age', 'Height']
column_names = rdf.columns
rdf.to_csv(r'C:\Users\rjakkula\Documents\DE\visualstudio\PythonSQL\postgres_table_data_csv2.csv', header=column_names)

