# Library
import psycopg2
import pandas as pd
from sqlalchemy import create_engine, text
import csv 
import xlsxwriter

# Define the database connection parameters
db_params = {
    'host': 'dsfsdfdsfdsf',
    'database': 'sdfsdfdsfsd',
    'user': 'sdfsdfdsfdsf',
    'password': 'dfsdfsdfsdfds'
}

engine = create_engine(f'postgresql://{db_params["user"]}:{db_params["password"]}@{db_params["host"]}:5432/{db_params["database"]}')

sheet1 = pd.read_sql_table('table', engine, schema='schema')
print(sheet1.columns)

sheet2 = pd.read_sql_table('mobile2', engine, schema='schema')
print(sheet2.columns)

with pd.ExcelWriter(r'C:\Users\rjakkula\Documents\DE\visualstudio\PythonSQL\report_data.xlsx') as writer:
    sheet1.to_excel(writer, sheet_name = 'encmbr')
    sheet2.to_excel(writer, sheet_name = 'employee')