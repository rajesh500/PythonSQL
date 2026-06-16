# Library
import psycopg2
import pandas as pd
from sqlalchemy import create_engine, text

# Define the database connection parameters
db_params = {
    'host': 'ec2-34-206-124-133.compute-1.amazonaws.com',
    'database': 'db5g29u2cel02j',
    'user': 'u61gjpmvjt5prl',
    'password': 'p6a67b3b89c0babe7005c17bd8e2af98551fcbdde9aae7f26fd80d45ad0d73024'
}

engine = create_engine(f'postgresql://{db_params["user"]}:{db_params["password"]}@{db_params["host"]}:5432/{db_params["database"]}')

df = pd.read_csv(r'C:\Users\rjakkula\Downloads\AttendanceData05202024_05262024.csv')
table_name ='ats_attended_records'
df.to_sql(table_name, engine, schema='lower_backup', if_exists='replace', index=False)
