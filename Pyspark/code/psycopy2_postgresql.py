import psycopg2
from psycopg2 import Error

try:
    connection = psycopg2.connect(user="sdfdfsdfsdf",
                                  password="sdfsdfsdfsd",
                                  host="sdfsdfsdfsdf",
                                  port="5433",
                                  database="sdfsdfsdfds")

    cursor = connection.cursor()
    # SQL query to create a new table
    create_table_query = '''CREATE TABLE schema.mobile2(ID INT PRIMARY KEY     NOT NULL, MODEL           TEXT    NOT NULL, PRICE         REAL); '''
    # Execute a command: this creates a new table
    cursor.execute(create_table_query)
    connection.commit()
    print("Table created successfully in PostgreSQL ")

    insert_query = ''' INSERT INTO schema.mobile2(ID, MODEL, PRICE) VALUES (1, 'Iphone12', 1100); '''
    cursor.execute(insert_query)
    connection.commit()
    print("Inserted")

except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")