from sqlalchemy import create_engine, text
import csv 
import xlsxwriter
import psycopg2
import pandas as pd
import db_connect_variables as db  # importing another py file

# calling class of imported py file
cal = db.DBConnection()
# calling method of imported py file
tpl = list(cal.creden())
# print first value
print(tpl[0])

engine = create_engine(f'postgresql://{tpl[2]}:{tpl[3]}@{tpl[0]}:5432/{tpl[1]}')
sheet1 = pd.read_sql_table('cr200_log', engine, schema='lower_backup')
print(sheet1)

print(sheet1.columns)

sheet2 = pd.read_sql_table('mobile2', engine, schema='lower_backup')
print(sheet2.columns)

with pd.ExcelWriter(r'C:\Users\rjakkula\Documents\DE\visualstudio\PythonSQL\report_data2.xlsx') as writer:
    sheet1.to_excel(writer, sheet_name = 'encmbr')
    sheet2.to_excel(writer, sheet_name = 'employee')