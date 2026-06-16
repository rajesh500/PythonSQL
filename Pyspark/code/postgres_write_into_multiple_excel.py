# Library
import psycopg2
import pandas as pd
from sqlalchemy import create_engine, text
import csv 
import xlsxwriter

# Define the database connection parameters
db_params = {
    'host': 'ec2-34-206-124-133.compute-1.amazonaws.com',
    'database': 'db5g29u2cel02j',
    'user': 'u61gjpmvjt5prl',
    'password': 'p6a67b3b89c0babe7005c17bd8e2af98551fcbdde9aae7f26fd80d45ad0d73024'
}

engine = create_engine(f'postgresql://{db_params["user"]}:{db_params["password"]}@{db_params["host"]}:5432/{db_params["database"]}')

sheet1 = pd.read_sql_table('cr200_log', engine, schema='lower_backup')
print(sheet1.columns)

sheet2 = pd.read_sql_table('mobile2', engine, schema='lower_backup')
print(sheet2.columns)

with pd.ExcelWriter(r'C:\Users\rjakkula\Documents\DE\visualstudio\PythonSQL\report_data.xlsx') as writer:
    sheet1.to_excel(writer, sheet_name = 'encmbr')
    sheet2.to_excel(writer, sheet_name = 'employee')