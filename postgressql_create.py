from sqlalchemy import create_engine, text
engine = create_engine('postgresql://u61gjpmvjt5prl:p6a67b3b89c0babe7005c17bd8e2af98551fcbdde9aae7f26fd80d45ad0d73024@ec2-34-206-124-133.compute-1.amazonaws.com:5433/db5g29u2cel02j')
connection = engine.connect()
my_query = text("CREATE TABLE batchsit.mobile(ID INT PRIMARY KEY  NOT NULL, MODEL TEXT  NOT NULL, PRICE  REAL)")
result = connection.execute(my_query)

