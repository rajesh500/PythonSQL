# test.py

import pyspark
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Dev").getOrCreate()

data = [("Android", ["Reading", "Sports", "Programming"])]
columns = ["platform", "Exp"]
df = spark.createDataFrame(data, columns)
df.show()
