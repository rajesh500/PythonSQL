# Library
import psycopg2
import pandas as pd
from sqlalchemy import create_engine, text

# Define the database connection parameters
db_params = {
    'host': 'sdasdasdfasdf',
    'database': 'dfsdfsdfdf',
    'user': 'dfsdfsdfdsf',
    'password': 'dfsdfdsfsdfsdf'
}


engine = create_engine(f'postgresql://{db_params["user"]}:{db_params["password"]}@{db_params["host"]}:5432/{db_params["database"]}')

df = pd.read_csv(r'C:\Users\rjakkula\Documents\DE2\DE\visualstudio\PythonSQL\Data\county_holidays_data.csv')
# position based column name rename
print('columns', df.columns)
 
df = df.rename(columns= {df.columns[0]: 'ID', df.columns[2]:'CREATED_DATE', df.columns[3]:'BEGIN_CLOSURE_DATE'})
table_name ='table'
df.to_sql(table_name, engine, schema='schemaname', if_exists='replace', index=False)


