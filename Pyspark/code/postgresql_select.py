from sqlalchemy import create_engine, text


engine = create_engine('postgresql://username:password@host:5433/db')
connection = engine.connect()
my_query = text("select * from schema.table limit 2")
result = connection.execute(my_query).fetchall()
for row in result:
    #print(row[1])
    print(row)

