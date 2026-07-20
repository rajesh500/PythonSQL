

# 1 Write a Python program to find the common elements between two lists

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

res = list(set(set(list1) & set(list2)))
#print(res)

# 2 Compare two CSV files and generate Insert, Update, and Delete records.
This can be solved using pyspark.

df1 = spar.read.format("csv").option("header", True).load("path")
df2 = spar.read.format("csv").option("header", True).load("path")

join both dataframes (full join because of delete statement, if id existing in target and not in source then delete it), when statement
if df1.id. == df2 then 'Update'
df1.id is not null and df2.id is null then 'insert'
df1.id is null and df2.id is not null then 'delete'


# 3. If JSON data has array and sub array, each array need to be explode, one after another one.
First array explode it and this result set need to explode it again.

{
    "customer_id": 101,
    "name": "Raj",
    "address": {
        "city": "Dallas",
        "state": "TX"
    },
    "orders": [
        {
            "order_id": 1,
            "amount": 250,
            "items": [
                {"product": "Laptop", "qty": 1},
                {"product": "Mouse", "qty": 2}
            ]
        },
        {
            "order_id": 2,
            "amount": 100,
            "items": [
                {"product": "Keyboard", "qty": 1}
            ]
        }
    ]
}


df = spark.read.option("multiline", "true").json("/Volumes/workspace/bronze/files/test.json")
df.show()

df1 = df.select("customer_id", "address.city", "address.state", "name", F.explode(F.col("orders")).alias("order"))
df2 = df1.select("customer_id", "city", "state", "name", "order.order_id", "order.amount", F.explode(F.col("order.items")).alias("item"))
df3 = df2.select("customer_id", "city", "state", "name", "order_id", "amount", "item.product", "item.qty")

+-----------+------+-----+----+--------+------+--------+---+
|customer_id|  city|state|name|order_id|amount| product|qty|
+-----------+------+-----+----+--------+------+--------+---+
|        101|Dallas|   TX| Raj|       1|   250|  Laptop|  1|
|        101|Dallas|   TX| Raj|       1|   250|   Mouse|  2|
|        101|Dallas|   TX| Raj|       2|   100|Keyboard|  1|
+-----------+------+-----+----+--------+------+--------+---+



# 4  Count the frequency of every word in a large text file.

d = {}
with open("/Volumes/workspace/bronze/files/file.txt", "r") as data:
    file = data.readlines()
    for i in file:
        a = i.rstrip('\n')
        for j in a.split():
            d[j] = d.get(j, 0)+1
print(d)

#     for file in data:
#         a = file.split()
#         for i in a:
#             d[i]=d.get(i, 0) + 1
# print(d)


#5   Merge multiple CSV files into a single output efficiently.

import glob 
import shutil
files = glob.glob("/Volumes/workspace/bronze/files/multipleFiles/*.csv")
with open("/Volumes/workspace/bronze/files/multipleFiles/merge.csv", 'wb') as data:
    filewrite = True
    for i in files:
        with open(i, 'rb') as idata:
            # write first file data
            if filewrite:
                shutil.copyfileobj(idata, data)
                filewrite = False # second file this condition will fail
            else:
                idata.readline()    # header 
                data.write(b"\n")   # write second file data into new line
                shutil.copyfileobj(idata, data)

























