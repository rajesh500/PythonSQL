import psycopg2
from psycopg2 import Error

try:
    connection = psycopg2.connect(user="u61gjpmvjt5prl",
                                  password="p6a67b3b89c0babe7005c17bd8e2af98551fcbdde9aae7f26fd80d45ad0d73024",
                                  host="ec2-34-206-124-133.compute-1.amazonaws.com",
                                  port="5433",
                                  database="db5g29u2cel02j")

    cursor = connection.cursor()
    # SQL query to create a new table
    create_table_query = '''CREATE TABLE lower_backup.mobile2(ID INT PRIMARY KEY     NOT NULL, MODEL           TEXT    NOT NULL, PRICE         REAL); '''
    # Execute a command: this creates a new table
    cursor.execute(create_table_query)
    connection.commit()
    print("Table created successfully in PostgreSQL ")

    insert_query = ''' INSERT INTO lower_backup.mobile2(ID, MODEL, PRICE) VALUES (1, 'Iphone12', 1100); '''
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