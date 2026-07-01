## Process 25 GB file/how to choose cluster size/no of partition/tasks ...

spark job process 25GB file, how much a cluster configuration is required.
25GB = 25 * 1024 MB = 25600 MB
no of partitions = 225600 /128 = 200 
no of cpu cores = no of partitions = 200

executors:
as per research for a better performance 2 to 5 cores required.
avg CPU cores for each executor = 4


excutor memory:
executor memory for each core = minimum 4 * parittion size = 4 * 128 = 512 MB

CPU cores for each executor = 4 * memory for each executor = 4 * 512 = 2 GB


total memory required to process 25 GB data?
total no of executor = 50
memory for each executor = 2GB
total memory for all the executor = 50 * 2 = 100GB

driver memory minimum 2 to 4 GB.



# 2 TB file:
1024 * 2048 GB = 2097125 / 256MB (default partition size).
8091 task or partition will run.

spark will run on waves when more tasks than available CPU cores.
waves means 
wave1:
task1 --> core1
task2 --> core2
.....
task10 --> core10.
wave2
task11 --> core1
...

Example if cluster size is 16 workers/execute each has 16 cores
totally 256 cores 

32 * 256 = 8091 tasks will be process in 32 waves.



## one files is 100 MB and another is 1GB, how do we process in pyspark.
Using broadcast join we will process this
100MB files using as broadcast dataframe.
1GB is regualr another dataframe.

Broadcast join will keep this 100 MB file in all the executor to avoid the shuffling.
Default broadcast file size is 10MB but we can increase it up to 500MB


## how do you handle small file problem.
1. during writing into target repartition or coalesce mention the required no of partition files, data will load into those no of files only.

Here we have an issue after process the data, before writing all the data need to be come into one node.
some data will write into disk after the ram memory then writing operation will be slow and cluster has to run untill the job is done.  some time it causes OOM as well.
Hence compute cost will increase. Instead of this if we use weekly job to move multiple files into single file per day.
here we will select small size cluster and writing into a single file will be done in 5 minutes. hence we will save here 
compute time.


## compresion file size is unsplittable how do process it fast.
even though compression format doesn't support to split into multiple files.
if we define as repartition(10) after reading data into dataframes then 10 partitions will be created and process in 10 tasks. here also we can achieve parallelism.

## Lazy evalution
save, collection untill these kind of operation is called transformation is delayed.

pyspark architecture is master-slave architecture.
has three main components.

1. driver (master)  (create spark context)
2. cluster manager
3. executor (slaves)


Executor: 
job  --> triggered by action (count(), save()).
stage --> stages 
task  --> One task is created for each data partition and sent to an executor for processing



## AQE (Adaptive  Query Execution):
Adaptive Query Execution (AQE) in Apache Spark 3.0+ is a dynamic optimization framework that re-optimizes query plans during runtime based on statistics from completed stages. By adjusting partition sizes, join strategies, and handling data skew on the fly, AQE significantly reduces manual tuning and improves performance. It is enabled by default in Spark 3.2.0 and later.


without AQE spark default partitions are 200. Hence excessive shuffling
and to many small files creates.

With AQE during the runtime it will handle partitions 
Coalescing partitions: Combining small partitions after a shuffle.
Converting joins: Switching to a Broadcast Hash Join if one side becomes small enough.
Handling skew: Splitting skewed partitions to balance workload.

AQE is enabled by setting spark.sql.adaptive.enabled to true (default in 3.2.0+). 



## Spark job submitted:
Once a Spark job is submitted via spark-submit, a Driver program is launched, which converts the application code into a logical Directed Acyclic Graph (DAG) of tasks. The driver requests resources from the Cluster Manager (YARN, Kubernetes, or Spark Standalone), which launches executors on worker nodes, distributes tasks, monitors execution, and collects results.


## Predicate pushdown:
Predicate pushdown is a performance optimization technique in Apache Spark that moves filtering logic (predicates) directly to the data source rather than loading all data into Spark's memory first. By evaluating filters at the storage layer, Spark significantly reduces I/O, network traffic, and memory consumption.


## parquet file:
columnar-oriented data storage designed for high-performance data processing in Hadoop ecosystem.
Parquet organizes data by columns, which enables efficient compression and faster analytical queries.

Key Features:
columnar storage, schema evolution, efficient compression, ownschema and metadata, complex data support.

Limitations:
No ACID transactions, Not for OLTP, Immutability, schema inflexibility(You cannot rename, reorder, or drop columns without a full table rewrite).


## Life cycle of spark application:
client --> cluster manager  <------> driver -----> worker node -----> execute ---> task 

driver ---> break down jobs into stages --> each stage a task creates---> task sent to cluster 
---> worker node receive task from driver ---> execute the task parallel on executors and return the result to driver --> collect all data and aggregate them into the final output --> return to client --> once the execution is completed driver program shutdown.
cluster manager release the resource and it is available to other applications.


cluster manager and driver will communicate the launch the worker node.
data will be available at  worker node and code sent to each executor.


## reading a parquet and orc files are faster compared to csv
* if source is a file and those are multiple files then parallelism is achieve, reading and writing will be done very fast. (file is csv, parquet, orc).
* If the file is compressed and that compression format support splitibility then parallelism achieve,  reading and writing will be done very fast
* If a file is very large and it is single file then still parallelism achieve based on file format. If the file is csv by default it is splitiable and parallelism achieved,  reading and writing will be done very fast.

or once data is read, repartition() it will no of cores  parallelism will be achieve .

* if the file is compressed and compression format doesn't support splittable then reading will be done in 1 core.
as well as writing will also be done in one core. 


## Delta vs Delta live table
🔹 Delta Table – The foundation
A storage format powered by Delta Lake, giving you:
✅ ACID transactions
✅ Time travel for historical queries
✅ Schema enforcement & evolution
✅ Efficient upserts and deletes

🔹 Delta Live Table – The orchestrator
A managed ETL pipeline framework that:
✅ Automates table creation & updates
✅ Manages dependencies between tables
✅ Ensures data quality with built-in expectations
✅ Supports Medallion Architecture (Bronze → Silver → Gold)



Delta live tables:
it is a declarative ETL framework that simplifies building, managing, and monitoring reliable data pipelines.
This pipeline itself handle data quality, error handling .....
which means do the transformation not back end orchestration..

delta live tables is available for only premium account.
delta live table has three options during pipeline creation core, advance, premium 
1. core is basic tranformation, no CDC
2. CDC, no governance, data quality etc...
3. premium has all the options.



## Idempotent:
If pipeline run's multiple time target should load with same data without duplicate.
if we maintain this in the pipeline is called Idempotent.
Ex: If we are processing data on a day basis, all of suddent pipeline is failed for today. How to load /rerun the pipeline with out loading duplicate in the pipeline.

if we achieve this in the pipeline it is called Idempotent.

1. 
Build a pipeline to fresh load and rerun should handle with in it.
if pipeline failed make an entry into the table, when re-running pass the target path with rerun as string
then delete the target data and rerun it. if the target is delta table.

If the target is file then delete and rewrite it.

2. 
If we don't delete the data or kind of scd-type2 implementation
use merge command to reprocess that data again without duplicates


## stable partition / rerun the pipeline
A large file is processing, in one of the partition data is failed then rerun the entire pipeline again because if 
you write data into the target with spark partition id, data processed in which partition and trying to run that specific partition is not possible. when you rerun partition id will change and data will not go into the same partition again.
this will cause a problem.

In order to achieve this kind of processing, define a  "stable_partition_id = deterministic bucket from a business key, reliable for rerun"
when you read data into dataframe and define data with stable partition then data will categories into that partition.
df = df.withColumn("stable_partition_id", F.pmod(F.xxhash64("order_id"), F.lit(10)))
count data based on stable partition id and store in temporary df.

Now data will process on spark partition and write into table.
once data write into table compare temporary df count and target table count based on stable partition id.
Once match pipeline completed sucessfully. if it is failed then pick that stable partition id
and filter out from source data frame based on this partition id and reprocess it.

C:\Users\rjakkula\Documents\DE2\DE\visualstudio\PythonSQL\Pyspark\Pipeline_design_code\stable_partition_handle.py


## deduplication.
pyspark remove duplicate based on business key.
dropDuplicates(),assign a row number and filter 1

## serving layer
The serving layer is the part of a data platform where data is prepared for consumption by end users.



https://www.youtube.com/watch?v=VQzn-8XKWg4&list=PLp8qtTIke0EWuaQm3vZMwQgxflC6NBU8y



## Masking data:
dynamic masking is directly not an option in pyspark.
dynamic masking can be done using databricks.

static masking:
can be done by using a variable, need to pass true/false value to this variable, based on this user can view the data.
df..withColumn( "ssn_masked", F.when(F.lit(viewer_can_see_pii), F.col("ssn")) 
.otherwise(F.concat(F.lit("XXX-XX-"), F.expr("right(ssn, 4)"))))

## encryption in pyspark:
Using cryptography library

from pyspark.sql.functions import udf, lit, col
from cryptography.fernet import Fernet
df.withColumn("encrypted_mail_id", encrypt_udf(col('mail_id'), lit(Key))) 
Note: key need to generate and pass it in the with column.

create a udf to encrypt and generate a key, pass key and data to udf then it will return a encrypted string.

similary decrypt the data.

SHA-256 hashing is another encrption technique.

from pyspark.sql import functions as F
# Apply SHA-256 to a column named 'sensitive_data'
df_hashed = df.withColumn("hashed_col", F.sha2(F.col("sensitive_data"), 256))
df_hashed.show()



## Data bricks masking:
dynamic masking:
is_account_group_member() based on this, if the user is part of the group, they can view the masking data.
If the user is part of admin group they can view base table data.

CREATE OR REPLACE FUNCTION email_mask(email STRING)
  RETURN CASE
    WHEN is_account_group_member('auditors') THEN email
    ELSE regexp_replace(email, '^.*@', '***@')
  END;

ALTER TABLE users ALTER COLUMN email SET MASK email_mask;


RBAC: role based access control (create a group add access to it , create a user tag that user to group).
ABAC: Attribute based access control.
create a governaced tag and tag this to user.
means: creating a access control at field level. this field level access can be done using creating a tag.
this tag tag to user, then apply masking when user query table this field data he can view as masking data.




## Scenario's
Scenario's pipeline tunned or optimization in spark job. Recent tunning or optimization in spark job.

1. Small File problem
2. Data Skewness
3. Broadcast join
4. multiple columns


## Small File problem:
Causes:
High Partition Count / Low Data Volume: 
Spark often defaults to 200 shuffle partitions (spark.sql.shuffle.partitions), which is suitable for large datasets but creates 200 small files if the dataset is only a few megabytes.

Streaming/Micro-batching: 
In Structured Streaming, every micro-batch writes new files. If the trigger interval is short, thousands of tiny files are created hourly.
Over-Partitioning (partitionBy): 
Partitioning by high-cardinality columns (e.g., user_id or timestamp) creates thousands of subdirectories, each likely containing only a few kilobytes of data.

Many-to-One Joins/Transformations: 
Operations that skew data or reduce its size before writing, without reducing the partition count, lead to files that are mostly empty.

Every day batch processing around 100GB data and running time around 20 minutes. 
All of sudden it took 2.5 hours.

Debugging: spark UI, during reading 1000 thousand of partitions created, resulting each file size come around 6 MB.
thousand of file information has to keep in metadata, here itself GC over memory head issue will occur. but come some how
to many small files created.

I increased the maxparitionbytes to 128 it is default one, still setup this config then job took 30 minutes to completed it.
spark.conf.set("spark.sql.files.maxPartitionBytes", 128 * 1024 * 1024).



Optimization can be done at cluster level and code level.



## Multiple columns:
Current job is running 5 hours of time from the begining of this pipeline in the production.
Business team requested is their a way to reduce this job running time.

I have checked the code and cluster level to optimize it but i couldn't see any issue.
i requested business team to add more resource, even same approach they got it from another SME.
I took it as chanllenge and looked again and started running the job and looked at spark UI.
after some long time i see the job in spark UI. this makes me to look into the code again.

I observed a for loop code which is adding 300 new columns to dataframe using withColumn, here it is causing issue.
when we add a new columns with withColumn every time it has create a new logical plan for every column hence here
it is taking time.

I removed that specific piece of code and write with select statement using list comphrension. Now all the column added one time to the data frame and only one new logical plan creates it. Hence job run is completed in 1 hours.



Data Skew vs Data Spill:
Data skew uneven distribution of data across partitions.
Data spill memory overflow where data is written to disk because it exceeds RAM.

## data skewness and data spill.
We have sitution like data is skewness in multiple partitions and data spill writing to disk.
We have a problem, were we need to assign a rank to the data based on each department and we have some duplicate data.
When a dense_rank applied with regualr window function for each department, noticed both the issues in UI.
This is happening because of one department has more data then this department data went to a partition.
similary some other partition has more data.

In order to fix problem what i did is, get only the distinct data and assign a rank to it.
and then join with main dataset, since then duplicate rank are assigned from the above rank because both of them are having same ID. hence data spill and skewness didn't occured. 

Hence achieve a better performance.


## data skewness:
uneven distribution of data can cause this problem.
Fix it using AQE


## col:
col is used for a column from the data frame.
when applying functions or transformations .alias(), .cast(), .asc(), desc()
col("a")+col("b"), conditional logic
column or column name from a variable


spark.sql.files.maxPartitionBytes	  vs   spark.sql.shuffle.partitions
When data is first read from file sources.  After wide transformations like join or groupBy.


## GC Error: (Garbage Collection):
A Garbage Collection (GC) error in PySpark, typically appearing as java.lang.OutOfMemoryError: GC overhead limit exceeded, indicates that the Java Virtual Machine (JVM) is spending more than 98% of its time on garbage collection while reclaiming less than 2% of the heap memory. 

Set configuration: --conf "spark.executor.extraJavaOptions=-XX:NewRatio = 2"   to fix it

Frequent Minor GCs --> increase youngGen(newSize)  NewRatio = 3...
Full GC often --> Increase oldGen (decrease NewRatio)

## Vacuum:
The VACUUM command in PySpark is used to remove stale, unused data files.





-----------------------------------------------------------------------------------------------------------------

pyspark2   -- start in itversity lab


Spark is processing  engine of big data.

Mapreduce is also a process engine for Hadoop Frame, but we have disadvantage for this one that why spark is famous

Hadoop   -> HDFS
         -> MapReduce (structure, semi-str, unstr) and code writen in java language
         -> Hive ( structure, semi-structure) and coding in hive query HQL
         -> pig  ( str, sem-str, unstru) coding in pig latin
         
         
         All these independent for programming language but all these working in the backend with MapReduce.
         
         
Spark is Alternative to MapReduce.



Difference between spark and MapReduce

Spark:
Structured
Semi-Structured
Un-Structured

MapReduce:
Structured
Semi-Structured
Un-Structured

Spark1:
Language Scala, Python, Java, R
   
MapReduce1:
Java( Preferred language)
C++
Python

Spark2:
SQL- Structured
     Semi-Structured
     
MapReduce2:
Java -> MR
HQL ->  Structured
        Semi-Structured
       
Spark3:
Real-Time Processing(Streaming Data)

Batch & Stream both can be used.

MapReduce3:
No  Real-Time Processing(Streaming Data)

Batch-Processing means divide data into Batches and then process.

       
Spark4:
In-Memory computation

MapReduce:
Not in-memory computation

Spark5:

 HardWare <-> RAM
   |           |
   ⬇          ⬇
Magnetic Disk  Semi-conductor memory  
   
Save data

If a file save in HardDisk and RAM retrieval is very fast in RAM when compared to HardDisk, because
of data stored in HardDisk is Magnetic Disk and  RAM in Semi-conductor.

MapReduce5:
Mostly data store in HardDisk and any operations.

Compared to other data processing language or tool
Hadoop is 10 times faster
Spark is 100 times faster.

Spark6:
Processing data can be happend from any ever example HDFS, LFS, amazon s3, HBASE, cassandra, flame, Kafka, RDBMS.

MapReduce6:
Processing the data only store in HDFS because MapR is tightly coupled with HDFS
(amazon s3, HBASE, cassandra, flame, Kafka, RDBMS all these can also be processed when we can move data to HDFS)

Spark7:
Yarn is standalone scheduling tool.
Mesos is scheduler.


MapReduce:
Yarn is used to scheduling the jobs


Hadoop is not mandatory to run the Spark Jobs
Spark can work with Hadoop or without Hadoop.


Spark vs Mapreduce:
MapReduce vs. Spark: Performance
Apache Spark processes data in random access memory (RAM), while Hadoop MapReduce persists data back to the disk after a map or reduce action. In theory, then, Spark should outperform Hadoop MapReduce. Nonetheless, Spark needs a lot of memory. Much like standard databases, Spark loads a process into memory and keeps it there until further notice for the sake of caching. If you run Spark on Hadoop YARN with other resource-demanding services, or if the data is too big to fit entirely into memory, then Spark could suffer major performance degradation.

MapReduce kills its processes as soon as a job is done, so it can easily run alongside other services with minor performance differences.

Spark has the upper hand for iterative computations that pass over the same data many times. But when it comes to one-pass ETL-like jobs — for example, data transformation or data integration — that's exactly when MapReduce excels.

Bottom line: Spark performs better when all the data fits in memory, especially on dedicated clusters. Hadoop MapReduce suits data that doesn’t fit in memory and can run well alongside other services.


Component of Spark:
1. Spark Core --> Unstructured
2. Spark SQL --> Structure, semi-structure
3. Spark Streaming --> Streaming data( str, un-str, semi-str)
4. Spark MLlib
5. Spark Graphics


Data storing object in spark:
1. Spark Core --> RDD(Resilient Distributed DataSet)
2. Spark SQL --> DataFrame|DataSet)
3. Spark Streaming --> DStream(discretized)
4. Spark MLlib  -> vectors
5. Spark Graphics  -> graph frames


RDD is also divided data into partition and do the parallel processing.
Partitions -> we can decided no of partitions (full control)
no partition size is to be set.


MR: HDFS -> Files
             ⬇
           blocks
           
Hive - tables
pig - bags

blocks we cant have control

               

RDD:
** no replication of data in the Spark
If data is lost while processing to continue the processing, it will regenerate the lost data this feature is called RDD.


Pipelining: (Parallel Processing)

                    filter         map1          map2
100 records          1              1             1
sys1                 2
                     3
sys2

sys3



Here how parallel processing is happing, first records will process and pass it to map mean while second will also processing from filter and result will pass to map1
.. All records won't wait till the filter logic to be completed, process the first and map result it second level it wont wait to come all records what the records it received it will process
like this parallel processing will be happened.


Same example Hadoop will complete first filter logic and pass to second level.



Reading files in apache spark and pyspark both are same, only difference is in apache spark 
val df = spark.read.format("csv").load("hdfs:///user/rajeshjkv5/finance_data.csv")

pyspark

df = spark.read.format("csv").load("hdfs:///user/rajeshjkv5/finance_data.csv")

Reading  orc file:
orc_df = spark.read.format("orc").orc("hdfs:///user/rajeshjkv5/userdata1_orc")

note: avro is pending?

pyspark2 --packages com.databricks:spark-avro_2.11:4.0.0



Read a File:
df = spark.read.format("csv").option("header", "true").load("file:///home/biglearner/df_csv_data.csv")
df = spark.read.format("csv").option("header", "false").load("file:///home/biglearner/df_csv_data.csv")
df = spark.read.format("json").load("file:///home/biglearner/DataFrame_data.json")   -- These files are in hdfs location.

csv from local:
csv_data = spark.read.csv("/Users/rajeshjakkula/Documents/spark_datafile/finance_data.csv")

json from local:
multiline_df = spark.read.json("/Users/rajeshjakkula/Documents/spark_datafile/employees_singleLine.json")
multiline_df1 = spark.read.option("multiline","true").json("/Users/rajeshjakkula/Documents/spark_datafile/employee_multiLine.json")

parquet file from local:
df =spark.read.parquet("/Users/rajeshjakkula/Documents/spark_datafile/userdata1.parquet")
df.write.parquet("/Users/rajeshjakkula/Documents/spark_datafile/people.parquet") 

df.write.mode('append').parquet("/tmp/output/people.parquet")
df.write.partitionBy("gender","salary").parquet("/tmp/output/people2.parquet")


df1 = spark.read.format("delta").option("timestampAsOf", timestamp_string).load("/tmp/delta/people10m")
df2 = spark.read.format("delta").option("versionAsOf", version).load("/tmp/delta/people10m")


Read compression file:
df = spark.read.csv("filepath/part-000.csv.gz", header=True, schema=schema)


write a File:
wrt_df.write.format("csv").save("/Users/rajeshjakkula/Documents/spark_datafile/writing_into_csvfile.csv") 
wrt_df.write.format("json").save("/Users/rajeshjakkula/Documents/spark_datafile/writing_into_csvfile.json")
wrt_df.write.format("avro").save("/Users/rajeshjakkula/Documents/spark_datafile/writing_into_avro_file.avro")

csv file compression:
filter_df.write.format("csv").option("codec", "gzip").save("hdfs:///user/rajeshjkv5/hdfs_datafiles/compressed_csvfile_gzip")  -- gzip
filter_df.write.format("csv").option("codec", "snappy").save("hdfs:///user/rajeshjkv5/hdfs_datafiles/compressed_csvfile_snappy")  -- snappy
filter_df.write.format("csv").option("codec", "deflate").save("hdfs:///user/rajeshjkv5/hdfs_datafiles/compressed_csvfile_deflate")  --deflate
filter_df.write.format("csv").option("codec", "BZip2").save("hdfs:///user/rajeshjkv5/hdfs_datafiles/compressed_csvfile_bzip2")  --BZip2
filter_df.write.format("csv").option("codec", "LZ4").save("hdfs:///user/rajeshjkv5/hdfs_datafiles/compressed_csvfile_lz4")  --LZ4


json file compression
filter_df.write.format("json").option("compression", "gzip").save("hdfs:///user/rajeshjkv5/compressed_json_dir/compressed_csvfile_gzip")  -- gzip
filter_df.write.format("json").option("compression", "snappy").save("hdfs:///user/rajeshjkv5/compressed_json_dir/compressed_csvfile_snappy")  -- snappy
filter_df.write.format("json").option("compression", "deflate").save("hdfs:///user/rajeshjkv5/compressed_json_dir/compressed_csvfile_deflate")  --deflate
filter_df.write.format("json").option("compression", "BZip2").save("hdfs:///user/rajeshjkv5/compressed_json_dir/compressed_csvfile_bzip2")  --BZip2
filter_df.write.format("json").option("compression", "LZ4").save("hdfs:///user/rajeshjkv5/compressed_json_dir/compressed_csvfile_lz4")  --LZ4

ORC file compression:
orc_df.write.format("orc").option("codec", "snappy").save("hdfs:///user/rajeshjkv5/compressed_orc_dir")

Parquet file compression:
orc_df.write.format("parquet").option("codec", "snappy").save("hdfs:///user/rajeshjkv5/compressed_parquet_dir")
orc_df.write.format("parquet").option("codec", "gzip").save("hdfs:///user/rajeshjkv5/compressed_parquet_dir_gzip/")


Avro compression:
We can do it two ways 
one while launching spark we can run avro package (pyspark2 --packages com.databricks:spark-avro_2.11:4.0.0) and compress the file.
run this command spark.conf.set("spark.sql.avro.compression.codec", "snappy") and write into file  -- here we are defining compressed format
orc_df.write.format("com.databricks.spark.avro").save("hdfs:///user/rajeshjkv5/compressed_avro_dir3/")

Note: In avro, we don't have any extension for compressed file still it is with .avro 
If we need to find weather it is compressed or not again we have to run the 
spark.conf.set("spark.sql.avro.compression.codec", "uncompressed") and write into file
orc_df.write.format("com.databricks.spark.avro").save("hdfs:///user/rajeshjkv5/compressed_avro_dir4/"). Now, compare both the files your able to see the difference 
on storage of the file.

spark.conf.set("spark.sql.avro.compression.codec", "snappy")   -- file compressed and save with   94616( 9KB)
spark.conf.set("spark.sql.avro.compression.codec", "uncompressed")  -- file compressed and save with 137081 (13KB)

second way:
second one runtime we can spark.conf.set("spark.sql.avro.compression.codec", "snappy")
and orc_df.write.format("com.databricks.spark.avro").save("hdfs:///user/rajeshjkv5/compressed_avro_dir/")    -- this way is not worked for me.


Textfile:
df=spark.read.format("text").load("/Users/rajeshjakkula/Desktop/unix_data_file.txt")
df.coalesce(2).write.format("text").mode("overwrite").save("/Users/rajeshjakkula/Desktop/pysparktxtformatwrite.txt")



examples:
dataframe.dropDuplicates() 
# Show title and assign 0 or 1 depending on title
dataframe.select("title",when(dataframe.title != 'ODD HOURS', 
1).otherwise(0)).show(10)

 df1.dropDuplicates(['City']).show() -- dropDuplicates at column level

# Show rows with specified authors if in the given options
dataframe [dataframe.author.isin("John Sandford", 
"Emily Giffin")].show(5)

ddf1.filter(df1.City.like('N%')).show()

dataframe.select("author", "title", dataframe.title.startswith("THE")).show(5)
dataframe.select("author", "title", dataframe.title.endswith("NT")).show(5)

dataframe.select(dataframe.author.substr(1, 3).alias("title")).show(5)
dataframe.select(dataframe.author.substr(3, 6).alias("title")).show(5)
dataframe.select(dataframe.author.substr(1, 6).alias("title")).show(5)

dataframe_remove = dataframe.drop("publisher", "published_date").show(5)
df.where("tweet is null").count()
df.where("tweet is not null").count()

# Replacing null values
dataframe.na.fill()      -- ALL null values it will replace with AA (df.select("tweet").na.fill("AA").show())
dataFrame.fillna()       --    same as na.fill()  stweet").fillna("AA").show()

# Returning new dataframe restricting rows with null valuesdataframe.na.drop()
dataFrame.dropna()
dataFrameNaFunctions.drop()   -- rp_df = df.drop("collected_at"), drp_df = df.drop("collected_at", "state_code")

# Return new dataframe replacing one value with another
dataframe.na.replace(5, 15)
dataFrame.replace()
dataFrameNaFunctions.replace()


where clause two conditional:
from pyspark.sql.functions import col, when
df.select("Education_Level", when(col("Education_Level") !="High School", 1).otherwise(0).alias("Rajesh")).show()

when_sdf = when_df.select("*", when(col("Education_Level") =  "Graduate", "College")
.when(col("Education_Level") = "High School", "School").otherwise("Unknown").alias("Example"))

when_sdf = when_df.select("*", when(col("Education_Level") ==  "Graduate", "College")
. when(col("Education_Level") == "High School", "School").otherwise("Unknown").alias("Example"))


Difference between Filter and Where:
According to spark documentation "where() is an alias for filter()"

Using filter(condition) you can filter the rows based on the given condition and where() is an alias for filter().

Filter is simply the standard Scala name for such a function, and where is for people who prefer SQL.


Joins:
CROSS JOIN:
The CROSS JOIN returns the dataset which is the number of rows in the first dataset multiplied by the number of rows in the second dataset. Such kind of result is called the Cartesian Product.
Prerequisite: For using a cross join, spark.sql.crossJoin.enabled must be set to true. Otherwise, the exception will be thrown


Inner Join:
Matching records from both tables

Left Join or Left outer Join: 
Both are same.


Right Join or Right Outer Join:
Both are same

Left Semi Join:
The LEFT SEMI JOIN returns the dataset which has all rows from the left dataset having their correspondence in the right dataset. 
Unlike the LEFT OUTER JOIN, the returned dataset in LEFT SEMI JOIN contains only the columns from the left dataset.


Left ANTI Join 
The ANTI JOIN returns the dataset which has all the rows from the left dataset that don’t have their matching in the right dataset. 
It also contains only the columns from the left dataset.

Examples:

ipl_df4 = ipl_df3.join(ipl_df1, "id")
ipl_df5 = ipl_df4.join(ipl_df1, ipl_df4.ide==ipl_df1.id)
ipl_df4 = ipl_df3.join(ipl_df1, "id" and "city")
ipl_df5 = ipl_df4.join(ipl_df1, ["id", "city"])



df = df1.join(df2, (df1.x1 == df2.x1) & (df1.x2 == df2.x2))
ipl_df5 = ipl_df4.join(ipl_df1, (ipl_df4.ide==ipl_df1.id)  & (ipl_df4.cite == ipl_df1.city))

ipl_df5 = ipl_df4.join(ipl_df1, ["id", "city"]) 
ipl_df5.count()
64
ipl_df5 = ipl_df4.join(ipl_df1, ["id", "city"], "left") 
ipl_df5.count()
64
ipl_df5 = ipl_df4.join(ipl_df1, ["id", "city"], "left_outer") 
ipl_df5.count()
64
ipl_df5 = ipl_df4.join(ipl_df1, ["id", "city"], "right_outer") 
ipl_df5.count()
816
ipl_df5 = ipl_df4.join(ipl_df1, ["id", "city"], "right") 
ipl_df5.count()
816
ipl_df5 = ipl_df4.join(ipl_df1, ["id", "city"], "full") 
ipl_df5.count()
816                                                                             
ipl_df5 = ipl_df4.join(ipl_df1, ["id", "city"], "full_outer") 
ipl_df5.count()
816
ipl_df5 = ipl_df4.crossJoin(ipl_df1) 
ipl_df5.count()
52224
ipl_df5 = ipl_df4.join(ipl_df1, ["id", "city"], "left_semi") 
ipl_df5.count()
64
ipl_df5 = ipl_df4.join(ipl_df1, ["id", "city"], "left_anti") 
ipl_df5.count()
0




Multiple Join conditions:]mpDF.join(addDF,["emp_id"]) \
     .join(deptDF,empDF["emp_dept_id"] == deptDF["dept_id"]) \
     .show()

#Using Where for Join Condition
empDF.join(deptDF).where(empDF["emp_dept_id"] == deptDF["dept_id"]) \
    .join(addDF).where(empDF["emp_id"] == addDF["emp_id"]) \
    .show()

Or 

#Using Where for Join Condition
empDF.join(deptDF).filter(empDF["emp_dept_id"] == deptDF["dept_id"]) \
    .join(addDF).filter(empDF["emp_id"] == addDF["emp_id"]) \
    .show()



Dataframe to rdd:
rdd1=df.rdd   -- this will convert data frame into rdd

RDD to dataframe:

toDF()
createDataFrame()

createGlobalTempView(name) -- Creates a global temporary view with this DataFrame. The lifetime of this temporary view is tied to this Spark application. 
createOrReplaceGlobalTempView(name)  -- Creates or replaces a global temporary view using the given name. The lifetime of this temporary view is tied to this Spark application.
createTempView(name)   -- Creates a local temporary view with this DataFrame. The lifetime of this temporary table is tied to the SparkSession that was used to create this DataFrame. throws TempTableAlreadyExistsException, if the view name already exists in the catalog.
createOrReplaceTempView(name)  -- Creates or replaces a local temporary view with this DataFrame. The lifetime of this temporary table is tied to the SparkSession that was used to create this DataFrame.


Dataframe to sparksql:
registerDataFrameAsTable(df, "table1")
registerTempTable()


createDataFrame():
Data in Python List, now converting it into RDD
list = [('Alice', '1')]
par = sc.parallelize(list)     -- Is RDD method
par.dtypes                     -- know data type
df = sc.createDataFrame(par)   __ converting RDD into DataFrame
df.show()
+-----+---+
|   _1| _2|
+-----+---+
|Alice|  1|                  -- If we didn't assign column name, it will take as _1, _2, _3 as column names
+-----+---+

df = spark.createDataFrame(par, ['Name', 'Age'])     -- creating a dataframe and column names as well
from pyspark.sql.types import *
schema = StructType([StructField("name", StringType(), True), StructField("age", IntegerType(), True)])    __ specifying column name and data types 
df = spark.createDataFrame(par, schema)            --  Another way of assigning column names

from pyspark.sql import Row
row_rdd = ("Name", "age")
df = spark.createDataFrame(par, row_rdd)         -- Another way of assigning column names
df.show()
+-----+---+
| Name|age|
+-----+---+
|Alice|  1|
+-----+---+

createGlobalTempView(name):
df.createGlobalTempView("people")
df2 = spark.sql("select * from global_temp.people")


createOrReplaceGlobalTempView(name):
df.createOrReplaceGlobalTempView("people")
df2 = df.filter(df.age > 3)
df2.createOrReplaceGlobalTempView("people")
df3 = spark.sql("select * from global_temp.people")


createTempView(name):
df.createTempView("people")
df2 = spark.sql("select * from people")

createOrReplaceTempView(name):
df.createOrReplaceTempView("people")
df2 = df.filter(df.age > 3)
df2.createOrReplaceTempView("people")
df3 = spark.sql("select * from people")


registerDataFrameAsTable(df, "table1"):
Note: This is available in sparksql not in DataFrame, here we are converting DataFrame into Sparksql and assigning take as table

sqlContext.registerDataFrameAsTable(df, "table1")
df2 = sqlContext.sql("SELECT field1 AS f1, field2 as f2 from table1")

Dropping Temp Table:
Three ways:
1. df.dropTempTable("tablename")
2. sqlContext.dropTempTable("table1")
3. Spark.catalog.dropTempTable("table1")
   spark.catalog.dropGlobalTempView("df")


Drop Nulls:
we have df.dropna()
na.drop()



df.explain(True) 
extended : True/False
mode  : simple, extended, code, formatted, codegen



isLocal():
isStreaming():
df.limit(2).show()
from pyspark import StorageLevel
df_AA.persist(StorageLevel.MEMORY_AND_DISK)
df.printSchema()
df.replace(10, 20).show()
df.selectExpr("age*2", "height*2").show()
df.sort("age")
df.sort("age", ascending=True).show()
.option("includeTimestamp", true)
df.select("*").orderBy(df.UNITS.asc()).show()
isNotNull()
isNull()
isin()


Select  vs selectExpr:

Select, simple we will select the columns, it select from data frame or sets
Example: df.select("ID", "Name", "last"). -- takes columns in string format
	df.select(col("ID")). -- columns type
	Can't take both.
Selectexpr, we can select the columns and do the certain expression at particular column level.
Here it takes SQL expression in string and return new data frame.
Ex:
df.Select("id", "Age" ).show(). --> select if we want to do expression kind as below can't be done in select statement, we need to use withColumn or case statement, or Expr statement.
   
df.selectExpr("id", "Age*2").show()     ---> age*2 is the expression

Repartitions: 
Repartitions can be used to increase and decrease number of partitions on the datasets.

Coalesce:
Coalesce can be used to only decrease the number of partition on the datasets.

Coalesce uses existing partitions to minimize the mount of data shuffling 
Example: let say you have four partitions
partitionA -> 1,2,3,4
partitionB -> 5,6 
partitionC -> 7,8 
partitionD -> 9, 10

newDf = df.coalesce(2)
PartA --> 1,2 3,4,7,8
partB --> 5,6, 9,10
Here, only partition moves from C -> A and D -> B

Coalesce avoid full shuffle
Coalesce may run faster than repartition 

DrawBack: or limitation:
However coalesce result in uneven, unequal sized  partition and spark will generally work slower with unequal sized partitions.


Repartition:
partitionA -> 1,2,3,4
partitionB -> 5,6 
partitionC -> 7,8 
partitionD -> 9, 10

newDf = df.repartition(2)
PartA --> 1,2 3,4,7,8
partB --> 5,6, 9,10

Here, the partition data is moved from B,C -> A and C -> D, so shuffling is less. 
The algo is repartition went for full shuffle to evenly distribute the data.

Repartition does full shuffle to make sure that the partitions are equally distributed.
That's the reason, Repartitioning  will always results in equal sized partitions.
spark works faster with equal sized partitions.


Note:
Spark RDD is immutability
Repartition and coalesce will create new RDD
The Base RDD will continue to have existence with its original number of partitions.


Example Data:
df = sc.parallelize([ Row(name='Alice', age=5, height=80), Row(name='Alice', age=5, height=80), Row(name='Alice', age=10, height=80)]).toDF()
df.show(

+---+------+-----+
|age|height| name|
+---+------+-----+
|  5|    80|Alice|
|  5|    80|Alice|
| 10|    80|Alice|
+---+------+-----+
df.replace(10, 20).show()

selectExpr:
df.selectExpr("age*2", "height*2").show()
+---------+------------+
|(age * 2)|(height * 2)|
+---------+------------+
|       10|         160|
|       10|         160|
|       20|         160|
+---------+------------+

sort:
df.sort("age")
df.sort("age", ascending=True).show()


Handling late data:
df.withWatermark("eventTime", "10 minutes")     Watermark means handling late data
Example:
12:00 to 12:10  at 12:10 watermark is 12:00 that means till the 12:00 clock data is finalized  and process it.
Once it start processing if any data comes before 12:00 it will drop but if data comes after 12:00 clock it will pick and process it.
or after 12:00 clock data will processes in next window.


window function examples:  (https://sparkbyexamples.com/pyspark/pyspark-window-functions/)
window functions are 

row_number()
rank()
dense_rank()
percent_rank()
ntile()
cume_dist() window function is used to get the cumulative distribution of values within a window partition.
sum()
max()
min()
first()
last() etc.....
https://sparkbyexamples.com/spark/spark-sql-aggregate-functions/

list_rdd= [('James", "Sales", 3000),
    ("Michael", "Sales", 4600),
    ("Robert", "Sales", 4100),
    ("Maria", "Finance", 3000),
    ("James", "Sales", 3000),
    ("Scott", "Finance", 3300),
    ("Jen", "Finance", 3900),
    ("Jeff", "Marketing", 3000),
    ("Kumar", "Marketing", 2000),
    ("Saif", "Sales", 4100)]

from pyspark.sql import Row
row_name=("employee_name", "department", "salary")
df=spark.createDataFrame(rdd, row_name)
df.show()    
    
row_number():    
from pyspark.sql.window import *
windowSpec= Window.partitionBy("department").orderBy("salary")   
from pyspark.sql.functions import row_number
df.withColumn("row_number_fun", row_number().over(windowSpec)).show() 
       or
df.withColumn("row_numer_func", row_number().over(Window.partitionBy("department").orderBy("salary"))).show()       
df.withColumn("row_num", row_number().over(Window.partitionBy("Group").orderBy("Date")))


rank():
windowSpec= Window.partitionBy("department").orderBy("salary")
from pyspark.sql.functions import rank
df.withColumn("rank_fun", rank().over(windowSpec)).show()


dense_rank():
from pyspark.sql.functions import dense_rank
df.withColumn("dense_rank_fun", dense_rank().over(windowSpec)).show()


percent_rank():
from pyspark.sql.functions import percent_rank
df.withColumn("percent_rank_fun", percent_rank().over(windowSpec)).show()


cume_dist():
from pyspark.sql.functions import cume_dist
df.withColumn("cume_dist_fun", cume_dist().over(windowSpec)).show()

CUME_DIST() = row / total number of rows

lead & lag:
from pyspark.sql.functions import lead, lag
df.withColumn("lead", lead("salary", 2).over(windowSpec)).show()
df.withColumn("lag", lag("salary", 2).over(windowSpec)).show()

NTILE() function in SQL Server is a window function that distributes rows of an ordered partition into a pre-defined number of roughly equal groups.
Ex: Suppose you have a result set that consists of 10 rows and you want to divide this result set into 4 buckets. First, 4 buckets will 2 rows are created. The remainder is 2 (10/4). These 2 buckets will be distributed to first and second buckets. As the result, the first and second buckets will have 2 + 1 = 3 rows. The last two buckets will have 2 rows.

SELECT ID,
NTILE (3) OVER (
ORDER BY ID
) Group_number
FROM geeks_demo;

Read from a table in dataframes:
path_to_data='/tmp/local/people/'
df=spark.read.format('delta').load(path_to_data)


Delta table:
path_to_data='/tmp/local/people.delta'
df=spark.read.format('delta').load(path_to_data)



Jdbc connection:
df=spark.read.format("jdbc").options(driver="org.mariadb.jdbc.Driver", user="tutorial_user", 
password="user_password",url="jdbc:mysql://singlestore.dbmstutorials.com:3306/tutorial_db",query="SELECT * FROM emp WHERE deptno=10").load()



Pending Topics:
spark out of memory?
spark executor tuning?
avro vs parquet file & orc vs parquet file?
spark dataset is typesafe?
dynamic resource allocation?
executor vs executor core?
performance tuning?
spark context?
catalyst optimizer?
spark lineage vs DAG?
map vs map partitions?
spark vectorization?
spark drivers vs executors?
AggregateByKey vs combineByKey?
spark vs yarn fault tolerance?
spark UDF?
broadcast join?
memory management?
client mode vs cluster mode 
spark context vs spark session
executor memory?
driver memory?

executor setup?
cluster setup?

Incremental data handling or CDC?
SCD type-2?


Row-format vs column format: (https://blog.matthewrathbone.com/2019/11/21/guide-to-columnar-file-formats.html)
For example, I have a table having two columns
Id, Name
1   Jack
2 Mathew
3 king
4 John

Data will be represented in row format is  1  Jack  2 Mathew 3 king 4 John    -- this is most human readable format
but in column format it is 1 2 3 4 ... Jack Mathew king John

When we open row format data in excel it seams to be good view but column format it is n't in good view.
However CCSV has a couple of useful properties that make it better for computers, and I’ll talk about those now.

Benefits of Columnar format:
READ-OPTIMIZATION:
SELECT COUNT(1) from people where Name = "Jack"
With a regular CSV a SQL engine would have to scan every row, parse each column, extract the last_name value, then count all Rathbone values that it sees.

In CCSV, the SQL engine can skip past the first two fields and simply scan line 3, which contains all the last name values available

COMPRESSION IMPROVEMENTS
Storing like-data together also has advantages for compression codecs. Many compression codecs (including GZIP and Snappy) 
have a higher compression-ratio when compressing sequences of similar data. 
By storing records column-by-column, in many cases each section of column data will contain similar values — that makes it ripe for compression. 
In fact, each column could be compressed independently of the others to optimize this further.

Negatives of Columnar Formats
The biggest negative of columnar formats is that re-constructing a complete record is slower and requires reading segments from each row, one-by-one

ORC vs parquet: 
http://www.differencebetween.net/technology/difference-between-orc-and-parquet/

ORC, short for Optimized Row Columnar, is a free and open-source columnar storage format designed for Hadoop workloads
As the name suggests, ORC is a self-describing, optimized file format that stores data in columns which enables users to read and decompress just the pieces they need
It takes significantly less time to access data and also reduces the size of the data up to 75 percent

ORC provides many advantages over other Hive file formats such as high data compression, faster performance, 
predictive push down feature, and more over, the stored data is organized into stripes, which enable large, efficient reads from HDFS. 

Parquet:
Parquet is yet another open-source column-oriented file format in the Hadoop ecosystem backed by Cloudera, in collaboration with Twitter
Like ORC, Parquet provides columnar compressions saving you a great deal of storage space while allowing you to read individual columns 
instead of reading complete files.
It is more efficient at doing data IO style operations.
particularly designed keeping nested data structures in mind
Parquet is also a better file format in reducing storage costs and speeding up the reading step when it comes to large sets of data

ORC                                                                           parquet
ORC was inspired from the row columnar                          inspired from the nested data storage format outlined in the Google Dremel paper
format which was developed by Facebook                          and developed by Cloudera, in collaboration with Twitter.

ORC only supports Hive and Pig                                  While Parquet has a much broader range of support for the majority of the projects in the Hadoop ecosystem
                                                                Parquet works really well with Apache Spark


ORC files are organized into stripes of data, 
which are the basic building blocks for data and are independent of each other.
Each stripe has index, row data and footer.

                                                                 Parquet, on the other hand, stores data in pages and each page contains header information, 
                                                                 information about definition levels and repetition levels, and the actual data.
spark, hive vectorization:
columnar format is must for using vectorization.


Avro file format:
Apache Avro
Avro is a row-based storage format for Hadoop which is widely used as a serialization platform. 
Avro stores the data definition (schema) in JSON format making it easy to read and interpret by any program. 
The data itself is stored in binary format making it compact and efficient. 
A key feature of Avro is robust support for data schemas that change over time - schema evolution. 
Avro handles schema changes like missing fields, added fields and changed fields; as a result, 
old programs can read new data and new programs can read old data. 
This format is the ideal candidate for storing data in a data lake landing zone, because:

Data from the landing zone is usually read as a whole for further processing by downstream systems (the row-based format is more efficient in this case);

Downstream systems can easily retrieve table schemas from files (there is no need to store the schemas separately in an external meta store);

Avro data format successfully handles line breaks (\n) and other non-printable characters in data (for example, a string field can contain formatted JSON or XML file);

Any source schema change is easily handled (schema evolution).



Parquet vs avrò vs orc:
Parquet 
Column oriented storage format
Schema is store in the footer of the file
Due to merging of scheme cross multiple files, schema evolution is little expensive
Ideal for read heavy data operations
Excellent for selected column data consumption and processing
Works excellent with spark as there is vectorized reader for parquet

Partially split-ability
Most efficient to used in spark 

Avro:
Row oriented storage format
Schema is store as JSON within file
It is also a serialization and RPC framework
Excellent for schema evolution
Ideal for write heavy data operations
Excellent for entire row consumption and processing

Partially split-ability 
Most efficient to used in Kafka

ORC:
Column oriented storage format
Schema is store in the footer of the file schema evolution is limited to adding new columns
Ideal for read heavy data operations Excellent for selected column data consumption and processing
Works excellent with hive as there is vectorized reader for parquet

Partially split-ability 
Most efficient to used in Hive




Directed Acyclic Graph(DAG)
DAG in Apache Spark is a combination of Vertices as well as Edges. 
In DAG vertices represent the RDDs and the edges represent the Operation to be applied on RDD. 
Every edge in DAG is directed from earlier to later in a sequence.
When we call anAction, the created DAG is submitted to DAG Scheduler which further splits the graph into the stages of the task.


Explanation:
Dag is a cyclic graph of stages ( On the calling of Action, the created DAG submits to DAG Scheduler which further splits the graph into the stages of the task.)
For example, we have multiple RDD and their is a dependencies on few of the RDD's and final all these are submit to Catalyst optimiser through lineage, then a DAG will submit to DAG scheduler 
Which means what are the stages and which stage need to execute first and what the task need to run on the same machine.

Lineage: 
https://data-flair.training/blogs/rdd-lineage/

** simple way lineage is a logical plan and DAG is a physical plan.



What happens when a Spark Job is submitted?
When a client submits a spark user application code, the driver implicitly converts the code containing transformations and actions into a logical directed acyclic graph (DAG). 
At this stage, the driver program also performs certain optimizations like pipelining transformations and then it converts the logical DAG into physical execution plan with set of stages. 
After creating the physical execution plan, it creates small physical execution units referred to as tasks under each stage. Then tasks are bundled to be sent to the Spark Cluster.
The driver program then talks to the cluster manager and negotiates for resources. The cluster manager then launches executors on the worker nodes on behalf of the driver. 
At this point the driver sends tasks to the cluster manager based on data placement. 
Before executors begin execution, they register themselves with the driver program so that the driver has holistic view of all the executors. 
Now executors start executing the various tasks assigned by the driver program. At any point of time when the spark application is running, the driver program will monitor the set of executors that run. 
Driver program in the spark architecture also schedules future tasks based on data placement by tracking the location of cached data. 
When driver programs main () method exits or when it call the stop () method of the Spark Context, it will terminate all the executors and release the resources from the cluster manager.





Broadcast Join:  or Broadcast hash join
If one table is small and other table is large, broadcast join is the good for better performance.
Small table by default it is 10MB.

How joining will work without broadcast?
Basically, large table data will be split into multiple nodes and each node has some small quantity of data and joining activity is performing 
data need to be shuffle, this shuffling will cost performance issue to avoid it we will use broadcast join.

For example, if the file is greater than 10MB automatically it will be consider as sort merge join.

we can customize the file size( increase the file size and still we can use broadcast join)

from pyspark.sql.functions import broadcast

data1.join(broadcast(data2), data1.id == data2.id)

rdd.explain will give complete information.


Broadcast join:
spark: spark.conf.set("spark.sql.autoBroadcastJoinThreshold", -1)   we can disable the broadcast join.
spark: spark.conf.set("spark.sql.autoBroadcastJoinThreshold", 20487500)   increasing broadcast small table size or increase threshold value.
spark: spark.conf.set("spark.sql.autoBroadcastJoinThreshold", 10000000)   setting back broadcast table size to 10MB [

Enable sort merge join:
spark.sql.config(spark.sql.join.preferSortMergeJoin). 
working of spark driver and executor:
https://blog.knoldus.com/understanding-the-working-of-spark-driver-and-executor/


Sort merge vs broadcast join:
https://medium.com/swlh/spark-joins-tuning-part-1-sort-merge-vs-broadcast-a98d82610cf0

If we are joining the data with small file and large file concept we will use broadcast join which is very fast and takes less time to process it.
If we turn off the broadcast join and perform a left join the it will take more time to process it.
Internally, sortmergejoin will perform the joining operation first sort the data and perform the merge operation (means joining the both data frames).
Which will takes more time compared to broadcast join.


Skew join:
Data skew can severely downgrade the performance of join queries. This feature dynamically handles skew in sort-merge join by splitting 
(and replicating if needed) skewed tasks into roughly evenly sized tasks. It takes effect when both spark.sql.adaptive.enabled and spark.sql.adaptive.skewJoin.enabled configurations are enabled

spark logical and physical plan:
https://blog.knoldus.com/understanding-sparks-logical-and-physical-plan-in-laymans-term/

SparkContext: https://www.youtube.com/watch?v=qQ8pidVduBA&t=349s
Spark SparkContext is an entry point to Spark and used to programmatically create Spark RDD, accumulators and broadcast variables on the cluster.

Spark Context,
SQL Context,
Streaming Context,
Hive Context is not available in spark context, need to create separate context for these.

The SparkContext is used by the Driver Process of the Spark Application in order to NNN a cKJ   ommunication with the cluster and the resource managers in order to coordinate and execute jobs.



SparkSession is an entry point to underlying Spark functionality in order to programmatically create Spark RDD, DataFrame and DataSet.
All these context is available in spark no need to handle explicitly 

Why spark session:
Unifies all the different contexts in spark and avoids the developer to worry about creating difference contexts

But the big advantage is —> 
Handling of independent, isolated configurations for the spark application run, with the help of multiple spark sessions.

All spark sessions will point to the same spark context within spark application
But each spark session would have their own set of configurations, table, view and other properties.

Detail explanation refer to hand written notes.




Spark Memory Management:
Agenda:
What is spark memory management?
Memory usage categories?
Type of memory allocation?
Memory calculation
Spark-submit parameters example

What is spark memory management:
* Spark is an in-memory processing engine
* Allocation and usage of memory plays a vital role in spark
* Efficient Memory use is critical for good performance 
* Memory management is include storing intermediate state while doing task execution like joins or to store the broadcast variables
* Memory usage in spark largely falls under one of two categories:   
     Execution memory
     Storage memory


Execution memory:
* Execution memory is the memory used in computations( join, shuffling....)
* Execution memory is for short lives. As soon as we are done with the operation, we can go ahead and release it
* For example, a task performing sort operation, would need some sort of collection to store the intermediate sorted values.
* Computation in shuffles, joins and aggregations etc..

Storage Memory:
* Storage memory is used for cache or distributed data to the clusters.
* Stage memory are for long lives. This is where we cache the data
* Until the allocated storage gets filled, storage memory stays in place. LRU( Least Recently Used) eviction is used to spill the storage data.
* When it gets filled and least recently accessed objects in the cache will be evicted.


Unified memory space
Portion of it occupied for cache

Let say M is the size of Unified, if execution required more memory then it release for more memory for execution and less memory for storage, vice-versa

Type of memory allocation: Dynamic vs Static:
Static Allocation:
* Resource values are given as part of spark-submit command
* In Static allocation, spark application reserves CPU and memory upfront irrespective of how much it really uses at a time
* Spark request all resource at start of application and release at end
* When multiple Jobs are running on same cluster and hence fight among multiple applications to acquire required no of resource( Executors)
* To resolve this problem, spark came with solution of Dynamic Allocation


Dynamic allocation:
* The values of resources are picked up based on the requirement( size of data, amount of computations needed) and released after use.
* This means your application may give resource back to the cluster if they are no longer used and request them again later when there is demand.
* When multiple applications share resources in your spark cluster, Dynamic allocation request and remove resource dynamically at run-time

Enabling Dynamic allocation:
isDynamicAllocationEnabled: True/False
spark.dynamicAllocatoin.enabled to True
Spark.shuffle.service.enabled to true


Parameters in dynamic allocation:
Spark.dynamicAllocatoin.initialExecutors
Spark.dynamicAllocation.minExecutors
spark.dynamicAllocation.maxExecutors

Static and dynamic allocation while spark-submit: or Executor Tuning:

Spark-submit —master yarn-cluster \
—driver-cores2 \
—driver-memory 2G \
—num-executors 10 \
—executors-cores 5 \
—executor-memory 4G \
—conf spark.dynamicAllocation.minExecutors=5 \
—conf spark.dynamicAllocation.maxExecutors=30 \
—conf spark.dynamicAllocaton.initialExecutors=10 \ # same as —num-executors 10

—class com.spark.progranname \

Memory Calculation:
Number of Nodes- 6
Cores Per node - 16Core
RAM Per node - 112 GB
Total hardware - 6Node, 96 Cores, 672 GB

1 core and 1 GB is needed for OS and Hadoop Daemons per node
So we left with 15 cores, 111 GB RAM for each node
Let’s take 5 cores per executors at best practice
No of Concurrent task per executor = no of cores per executor

No of executors per node = total no of core per node/ no of cores per executor : 15/5=3

Total no of executors = No of nodes * Number of executors per node 6*3=18

Memory for each executor 111/3=37GB
This should also include memory overhead(10% of Executor memory)

So Each Executor memory = 37-2.60 ~34GB

Final Numbers:
Total executors - 18
Each Executor memory - 34GB


Spark.conf.set(“spark.sql.shuffle.partitions”,1000)   assigning number of partitions.
No of partitions based on no of cores in executors









spark executor memory:
In a worker node,we have 4 executors each one is 4core and 16GB RAM, based on number of core in executor parallel processing task will exist.
Let say, we have 4 core in executor we will have 4 parallel processing tasks.

                  Memory 
                   |
                   |
 memory overhead     execution & storage     reserved memory   user memory
 
 Memory overhead:
 reserved off-heap memory for JVM or 
 memory overhead is the amount of off-heap memory allocated to each executor. By default memory overhead is set to either 10% of executor memory or 384 whichever is higher
 
 
 off-heap:
 not frequently used object will be keep here.
 In normal memory, garbage collector will be cleaned up and again when even required it will recreate , to avoid this we will keep in off-heap memory.
 
 execution & storage discussed above:
 
 
 spark.driver.memory
 spark.driver.memoryOverhead
 spark.executor.memory
 spark.executor.memoryOverhead
 
 spark.memory.fraction(execution)
 spark.memory.storageFraction(storage)
 
 Let say, I have allocated 4GB for executor 
 memory overhead is 10% = 4*0.10=0.4
 total memory=4.4GB request from the resource manager
 
 0.4GB goes to overhead and 300MB to reserved memory
 remaining memory will be allocated equal to executor and storage memory
 
  refer notes for detail explanation. 


--> refer this link for spill and memory assignment in spark'
https://selectfrom.dev/spark-performance-tuning-spill-7318363e18cb



*** What happens when a Spark Job is submitted?
Below is the step which spark job follows once job get submitted:

# A standalone application starts and instantiates a SparkContext instance and it is only then when you can call the application a driver.
# The driver program asks for resources to the cluster manager to launch executors.
# The cluster manager launches executors.
# The driver process runs through the user application. 
# Depending on the actions and transformations over RDDs task are sent to executors.
# Executors run the tasks and save the results.
# If any worker crashes, its tasks will be sent to different executors to be processed again.
# Driver implicitly converts the code containing transformations and actions into a logical directed acyclic graph (DAG). 
# Spark automatically deals with failed or slow machines by re-executing failed or slow tasks. 

For example, if the node running a partition of a map () operation crashes, Spark will rerun it on another node; 
and even if the node does not crash but is simply much slower than other nodes, Spark can preemptively 
launch a “speculative” copy of the task on another node and take its result if that finishes.



*** When submitting a Spark job, I notice that a few tasks are relatively taking longer time to get completed. 
What could be the cause of this and how to resolve this issue?

When a Spark job is submitted, each worker node launches an executor. 
The data is read from the source into RDDs or Data Frames which can be considered a sort of big arrays with multiple partitions. 
Each executor can launch one or more tasks with each task mapping to a partition thereby increasing parallelism.

However in case, the data is skewed i.e. some of the partitions contain much larger data compared to others, 
then tasks operating on larger partitions can take much longer to complete than those which operate on smaller partitions.

Data skewness can arise due to multiple reasons e.g. say source contains user data for various countries. 
If the data is partitioned based on country then a partition for a country having a larger population will have more data leading to data skewness. 
A better way to handle this situation is to partition data based on a key which results in more balanced spreading of data.

Another way to handle this problem is to use repartition. 
Spark repartition does a full shuffle of data in RDD and creates new partitions with data distributed evenly. 
Since the data is more evenly spread now, tasks operating on partitions will take an equal amount of time to process now. 
Keep in mind that repartitioning your data is a fairly expensive operation.

Yet another option is to cache the RDD or Dataframe before heavy operations as caching helps optimize performance to a great extent.




Spark Performance tuning:

Data Serialization in spark:
Serialization plays an important role in the performance for any distributed application. By default spark uses java serializer

API selection:
# Spark introduced three type of API to work upon RDD, DataFrame, DataSet
# RDD used for low level operation with less optimized
# Dataframe is best choice in most of the situation due to it’s catalyst optimizer and Low garbage collection(GC) overhead.
# Dataset is highly type safe and use encoders. It uses tungsten for serialization in binary format.

Advance variable:
Broadcast join

Cache() and persist():
The difference among them is that cache() will cache the RDD into memory, whereas persist(level) can cache in memory, on disk, 
or off-heap memory according to the caching strategy specified by level. persist() without an argument is equivalent with cache().

Caching RDDs in Spark: It is one mechanism to speed up applications that access the same RDD multiple times. 
An RDD that is not cached, nor checkpointed, is re-evaluated again each time an action is invoked on that RDD. 
There are two function calls for caching an RDD: cache() and persist(level: StorageLevel). 
The difference among them is that cache() will cache the RDD into memory, whereas persist(level) can cache in memory, 
on disk, or off-heap memory according to the caching strategy specified by level.
persist() without an argument is equivalent with cache(). 
We discuss caching strategies later in this post. Freeing up space from the Storage memory is performed by df.unpersist().


Caching strategies (StorageLevel): RDD blocks can be cached in multiple stores (memory, disk, off-heap), in serialized or non-serialized format.

MEMORY_ONLY: Data is cached in memory only in non-serialized format.
MEMORY_AND_DISK: Data is cached in memory. If enough memory is not available, evicted blocks from memory are serialized to disk. 
This mode of operation is recommended when re-evaluation is expensive and memory resources are scarce.
DISK_ONLY: Data is cached on disk only in serialized format.
OFF_HEAP: Blocks are cached off-heap, e.g., on Alluxio [2].
The caching strategies above can also use serialization to store the data in serialized format. 
Serialization increases the processing cost but reduces the memory footprint of large datasets. 
These variants append “_SER” suffix to the above schemes. E.g., MEMORY_ONLY_SER, MEMORY_AND_DISK_SER. 
DISK_ONLY and OFF_HEAP always write data in serialized format.
Data can be also replicated to another node by appending “_2” suffix to the StorageLevel: 
e.g., MEMORY_ONLY_2, MEMORY_AND_DISK_SER_2. Replication is useful for speeding up recovery in the case one node of the cluster (or an executor) fails.
A full description of caching strategies can be found here.

df.cache() calls the persist() method which stores on storage level as MEMORY_AND_DISK, but you can change the storage level

The persist() method calls sparkSession.sharedState.cacheManager.cacheQuery() and when you see the code for cacheTable it also calls the same sparkSession.sharedState.cacheManager.cacheQuery()

that means both are same and are lazily evaluated (only evaluated once action is performed), except persist method can store as the storage level provided, these are the available storage level

NONE
DISK_ONLY
DISK_ONLY_2
MEMORY_ONLY
MEMORY_ONLY_2
MEMORY_ONLY_SER
MEMORY_ONLY_SER_2
MEMORY_AND_DISK
MEMORY_AND_DISK_2
MEMORY_AND_DISK_SER
MEMORY_AND_DISK_SER_2
OFF_HEAP



Clear cache:
Spark.catalog.clearCache()


From Pyspark import StorageLevel
Df.persist(StorageLevel.DISK_ONLY)



File Format selection:

Level of parallelism:
# Parallelism plays very important role while tuning  spark job
# Every partition ~ task requires a single core for processing
# There are two ways to maintain the parallelism
Repartition: gives equal number of partitions with high shuffling
Coalesce: Generally reduces the number of partition with less shuffling.



spark out of memory:
refer notes.



driver vs executor
Driver
Kind of main program,  start the spark context
all the logic is written in driver, driver shift that logic to worker with the help of spark context.

Executor will process the task( means rdd)
It is the place were code will execute 

Driver is controlling board



why spark dataset is type safe?
RDDs and Datasets are type safe means that compiler know the Columns and it's data type of the Column whether it is Long, String, etc....

But, In Dataframe, every time when you call an action, collect() for instance, then it will return the result as an Array of Rows not as Long, String data type.
In dataframe, Columns have their own type such as integer, String but they are not exposed to you. To you, it's any type. 
To convert the Row of data into its suitable type you have to use .asInstanceOf method.


In Apache Spark 2.0, these two APIs are unified and said we can consider Dataframe as an alias for a collection of generic objects Dataset[Row], 
where a Row is a generic untyped JVM object. Dataset, by contrast, is a collection of strongly-typed JVM objects.

Spark checks DataFrame type align to those of that are in given schema or not, in run time and not in compile time. 
It is because elements in DataFrame are of Row type and Row type cannot be parameterised by a type by a compiler in compile time so the 
compiler cannot check its type. Because of that DataFrame is untyped and it is not type-safe.

Datasets on the other hand check whether types conform to the specification at compile time. That’s why Datasets are type safe.



Querying on non existing column
Now, let’s see how DataFrame and Dataset behave differently when querying on non-existing column.

Let’s query on a salary column which is not present in DataFrame.

val empDataFrameResult1 = empDataFrame.select("salary")
org.apache.spark.sql.AnalysisException: cannot resolve '`salary`' given input columns: [age, department, id, name];;
'Project ['salary]
And we will get a Runtime error, salary cannot be resolve in given input columns: [age, department, id, name] and thrown AnalysisException.

In the case of Dataset we have the opportunity to get that error in compile time itself.

val empDatasetResult1 = empDataset.map(employ => employ.salary)
<console>:25: error: value salary is not a member of Employ
       val empDatasetResult1 = empDataset.map(employ => employ.salary)
                                                               ^
It throws a compile time error, value salary is not a member of Employ.


Example:
Explanation, with example 
let say we have a data and were you apply filter( lambda x:x>15).show()
on dataframe it will return an error because of dataframe data in Array of row format and each column has it own data type

were has in dataset with same data and same condition, 
it will execute the code and return result because of dataset data refers to datatype(compiler known the column and its data type)

Dataframe return an error in runtime itself
Dataset return an error in compile time itself.


executor vs executor core:
Executor is a process and  Executor core is thread

Executor will execute the task independently based on number of parallel processing is available in executor
parallel processing task is available based on number of cores in executors.


Falut tolerance:
Fault tolerance refers to the ability of a system (computer, network, cloud cluster, etc.) to continue operating without interruption when one or more of its components fail. ... Fault-tolerant systems use backup components that automatically take the place of failed components, ensuring no loss of service


 Or capability of recover from failure.

Let say we have submit a job then couple of data node are down, where my data is lie in the data node then will spark recover the data from failure node, it is called fault tolerance.
If we have replication of data on the other nodes then spark will automatically recover the data from those nodes.



Resource Manager: Runs on a master daemon and manages the resource allocation in the cluster.
Node Manager: They run on the slave daemons and are responsible for the execution of a task on every single Data Node.
Application Master: Manages the user job lifecycle and resource needs of individual applications. It works along with the Node Manager and monitors the execution of tasks.
Container: Package of resources including RAM, CPU, Network, HDD etc on a single node.


ResourceManager acts as the scheduler and allocates resources amongst all the applications in the system.
NodeManager takes navigation from the ResourceManager and it runs on each node in the cluster. Resources available on a single node is managed by NodeManager.



Multi_delimiter:
Reading a textFile:


df1=spark.read.text("/Users/rajeshjakkula/Documents/spark_datafile/multi_Delimiter.txt")
df=spark.read.csv("/Users/rajeshjakkula/Documents/spark_datafile/multi_Delimiter.txt")

# reading a textile and split the data with double delimiter, if we try to using option("delimiter", "#*") then it will throw an error saying multiple delimiter is not accepted in spark
# it will support only single delimiter
# reading header and split them and storing value in a variable, in filter skipping header and converting it into rdd and split them and convert it back into dataframes.
header=df1.first()[0]
print(header)
schema=header.split('#*')
print(schema)
df1.filter(df1['value']!=header).rdd.map(lambda x:x[0].split('#*')).toDF(schema).show()


# tried to do it directly but throwing an error.
df_to_rdd=df.rdd.map(lambda x:x.split("#*"))
abc=df.rdd.map(lambda x:x.split("#*")).toDF()


How spark handles slow and long running task in your spark application:
Explanation: let say we have a job and it is divided into two stages and each stages again divided into two tasks
     

                 Task1
     Stage1      Task2
Job   
     Stage2      Task3
                 Task4
Here we have two worker nodes and each node is running with two tasks, in Worker1 task1 is completed and worker2 task3 and task4 is completed, task2 is long or slow running job then
Speculative Execution is the one will reinstate the task2 in another node and mean while on the same node task2 is also running, what ever the task is completed first then other task will be killed and return the data to driver.

spark.speculation=True
Spark.speculation.interval=200. ( with in this time interval tasks should complete otherwise speculative execution will be run)
Spark.speculation.mulitplier=5
spark.speculation.quantile=0.75.   ( 75 % of task should complete then only speculative execution will be consider of there tasks)

 
How to optimised file validation in spark.
Modes of DataframeReader:
Here, we will get bad data while reading file itself we need to handle the file.
Example, in Bad_data_File.txt we have bad records in the scenes we are getting null for some of the records to handle these null we are going to use modes while reading file itself.

Modes:
PERMISSIVE DEFAULT MODE.  In this mode if data is having null, file will be read as it is
FASTFAIL.  If the file is having bad data then it will throw an error (example int field is having string 1uuu, 2udb, 3cb3. This field data type is integer then it will thrown an error).
DROPMALFORMED. If the file is having bad data(nulls) all the null records will be remove only good records will be loaded.


mode=spark.read.option("delimiter", ',').csv("/Users/rajeshjakkula/Documents/spark_datafile/Bad_data_File.txt", header=True)
mode=spark.read.option("mode", 'DROPMALFORMED').csv("/Users/rajeshjakkula/Documents/spark_datafile/Bad_data_File.txt", header=True)
mode=spark.read.option("mode", 'FAILFAST').csv("/Users/rajeshjakkula/Documents/spark_datafile/Bad_data_File.txt", header=True)


 mode=spark.read.option("delimiter", ',').csv("/Users/rajeshjakkula/Documents/spark_datafile/Bad_data_File.txt", header=True)
>>> mode.show()
+----------+-------+-----+
|     Sport| player|score|
+----------+-------+-----+
|   Cricket|  Rohit|  264|
|   Cricket|  kohil|  183|
|   Cricket|Sachine| null|
|   Cricket|    Bad| null|
|  Football|  messi|super|
|  Football|ronalod| null|
|Basketball|   shaq| null|
+----------+-------+-----+



 mode=spark.read.option("mode", 'DROPMALFORMED').csv("/Users/rajeshjakkula/Documents/spark_datafile/Bad_data_File.txt", header=True)
>>> mode.show()
+--------+------+-----+
|   Sport|player|score|
+--------+------+-----+
| Cricket| Rohit|  264|
| Cricket| kohil|  183|
|Football| messi|super|
+--------+------+-----+



mode=spark.read.option("mode", 'FAILFAST').csv("/Users/rajeshjakkula/Documents/spark_datafile/Bad_data_File.txt", header=True)
>>> mode.show()

Error

---> bad data itself we can write into external location or adding a column to existing dataframe

While reading file itself we can handle this.


Join two data frames:
Df1.union(df2).show()




Explode:
mode=spark.read.csv("/Users/rajeshjakkula/Documents/spark_datafile/explode.txt", header=True)


 from pyspark.sql.functions import explode
>>> df2 = df.select(df.name,explode(df.knownLanguages))
>>> df2.show()
+---------+------+
|     name|   col|
+---------+------+
|    James|  Java|
|    James| Scala|
|  Michael| Spark|
|  Michael|  Java|
|  Michael|  null|
|   Robert|CSharp|
|   Robert|      |
|Jefferson|     1|
|Jefferson|     2|
+---------+------+



posexplode_outer by using this we can view position of array data in the result dataset




Write modes:
ErrorIFExist
Append
Overwrite
Ignore



MergerSchema:   (read level use it)
Schema evolution change in through a data-frame.

Through a dataframe level If there any change or adding a new column to the data-frame. That data-frame data should sync with relevant data types. MergeSchema will help on this.


Read options:
https://dbmstutorials.com/pyspark/spark-read-write-dataframe-options.html



Catalyst optimiser:
https://www.databricks.com/glossary/catalyst-optimizer

The catalyst optimizer applies optimizations during logical and physical planning stages. 
It optimizes the query logically then generates a range of physical plans and selects the most efficient one based on a cost model.

Adaptive query Execution:
https://towardsdatascience.com/apache-spark-3-0-adaptive-query-execution-2359e87ae31f



Broadcast Variable:
Let say, we have a table which contains us population info and one of the column is having state codes and also there is lookup table, in this lookup table we will have state codes and full name of the states, by looking into this codes in lookup need to populated state full name.
If we do it regularly then for each state code worker node will connect to driver and cause performance issue.


By using broad cast variable( means lookup data will be taken into this broadcast variable), this broadcast variable will be shared all the worked nodes ( available in worker node memory)
And state need to match from main table to lookup it will direct retrieve from worker node memory and perfume the further operation, so it will cause good performance.

abc=sc.broadcast(lookuptabledata).  --- abc will be shared to all the worker nodes.

https://www.youtube.com/watch?v=43ahz6Ad_RM


What are Broadcast Variables?

Broadcast variables in Apache Spark is a mechanism for sharing variables across executors that are meant to be read-only. 
Without broadcast variables these variables would be shipped to each executor for every transformation and action, and this can cause network overhead. 
However, with broadcast variables, they are shipped once to all executors and are cached for future reference.

Broadcast Variables Use case
Imagine that while doing a transformation we need to lookup a large table of zip codes/pin codes. 
Here, it is neither feasible to send the large lookup table every time to the executors, nor can we query the database every time. 
The solution should be to convert this lookup table to a broadcast variables and Spark will cache it in every executor for future reference.

Accumulator:
For aggregating the information through associative and commutative operations, Accumulator variables are used. As an example, for a sum operation or counters (in MapReduce), we can use an accumulator. In addition, we can use Accumulators in any Spark APIs.
Here is an example, it also has an attribute called value as same as the broadcast variable, this attribute also stores the data and then it is used to return an accumulator value. However,  only in a driver program, it is usable.


So, an accumulator variable is used by multiple workers and returns an accumulated value, in this example.
num = sc.accumulator(1)
def f(x):
  global num
  num+=x
rdd = sc.parallelize([2,3,4,5])
rdd.foreach(f)
final = num.value
print "Accumulated value is -> %i" % (final)




Handling json format data:
Input file:
PartitionDate    Status      Request
2020-06-04     Internal     {"Response":{"MessageId":15432}}
2020-06-05     Eternal     {"Response":{"MessageId":15433, "Latitude":"100", "longitude":"123"}}

df=spark.read.option("header", True).option("escape", "\").option("multiline", "true").csv("file.csv"))
From pyspark.sql.functions import col, json_tuple, to_json, from_json
df.select("*", json_tuple("request", "Response")).drop("request")
  .select("*"), json_tuple("c0", "MessageId",  "Latitude", "longitude").alias("MessageId","Latitude", "longitude" ).drop(c0).show()

Here in table one of the column is having json data handling json data and populate it as regular data in the table, to do this we can use json_tuple
Or to_json or from_json.


Pivot:
from pyspark.sql.functions import max, struct

(df_data
    .groupby("id", "type", "date", "ship")
    .count()
    .groupby("id", "type")
    .pivot("date")
    .agg(max(struct("count", "ship")))
    .show())


Date in pyspark:
to_Date():
Convert string to Data format.

df.select(col("input"), to_date(col("input"), "MM-dd-yyyy").alias("date")).show().  -- while taking date column, it should be column format or string.


InferSchema vs pre-defined schema:
df=spark.read.option("header", True).option("delimiter", "|").csv("file_location").  === this file contain 156 records.
To read data in the file and display it takes 0.02seconds.

Note: Here, while reading a file it will consider all column as string columns. If all columns are consider as string column in production doing calculation will take time because of column data type.



df=spark.read.option("header", True).option("inferSchema", True).option("delimiter", "|").csv("file_location")
Here, inferSchema will assign all the relevant column data types to all columns, if a column contains integer it will take it as integer only.
To Assign datatype to column, inferSchema will read all the file and assign relevant datatype to the column.

To read data in the file and display it takes 0.95seconds.


From pyspark.sql.types import *
sch=StructType([StructFiled(column_name, IntegerType(), True),
                StructFiled(column_name, StringType(), True)])

Why StructType is required?
Because when we read a file then all the column data will be default consider it has string type.
Using structtype we are defining datatype of each column

Inferschema = True will display the columns data type as is per the data type of each column define in a file.


df=spark.read.option("header", True).option("delimiter", "|").schema(sch).csv("file_location")
Here, we are predefining datatypes of a columns.

To read data in the file and display it takes 0.39seconds.

Note: don't take inferSchema for relevant column data types, always recommended way is define column types in the code. Example: sch.



Q: I have a directory, had a multiple folder and each folder has multiple file, from all folder and all files need to read at once.
.csv("Path/Data*/file*.csv"))
.csv(["Data1/*.csv", "Data2/*.csv", "Data2/*.csv"])
.csv("Data[1-3]*/*.csv")
.csv("Data{1,2,3}*/*.csv")




Masking data: means SSN is secured right so we have store the info has like below
Original_ssn.   Masked 
987654321       9*******1. In such way, we can use any symbol.
https://tunetotech.com/Post.aspx?post=9


PartitionBy:
When we are writing data into file and store it then we can use partitionBy
df.write.option("header", True).mode("overwrite").partitionBy("DateOnly").csv("path")



df.rdd.getNumPartitions(). -- to get number of partitions  f 


Each partition how much data is stored:
from pyspark.sql.functions import spark_partition_id, asc, desc
df\
    .withColumn("partitionId", spark_partition_id())\
    .groupBy("partitionId")\
    .count()\
    .orderBy(asc("count"))\
    .show()

#data will be reshuffled to 10 partitions with 10 sharded files generated.



Read from partitioned data:
Now let’s read the data from the partitioned files with the these criteria:

Year= 2019
Month=2
Day=1
Country=CN
The code can be simple like the following:

df = spark.read.csv("data/example.csv/Year=2019/Month=2/Day=1/Country=CN")
print(df.rdd.getNumPartitions())
df.show()


Control Number of Records per PartitionFile:
df.write.option("header", True).option("maxRecordsPerFile",2).partitionBy("Team").mode("overWrite").csv("Team")

maxRecordsPerFile will give, no of records to the file.



Partition to a minimum files:
dfRepart.repartition(2).write.option("header",True) \.partitionBy("state") \.mode("overwrite") \.csv("c:/tmp/zipcodes-state-more")




BucketBy:
df.write.mode("overwrite").bucketBy(4, "column_name").saveAsTable("Table_name").    ---> 4 is number of bucket
df.write.mode("overwrite").bucketBy(4, "column_name").csv("path")


Spark out of memory issues:
Driver out of memory 
Executor out of memory

Driver out of memory:
1. collect() operation
When we apply collect operation then it will read all data from executor(multiple executors) and this data size might be more than driver memory then drive will go out of memory.

2. Broadcast join:
Let say you have two file in executor were you need to take these two file in broadcast join and keep a  copy of it in each executor then while applying broadcast join on these two files, 
These two files will come into drive will be combined the data as single file then this file size might be big then driver will go out of memory.

how can we avoid it
Increase the driver memory or we can reduce the threshold limit for the broadcast table and table should be small  certain size.



Executor out of memory:
1. Off-heap memory or yarn memory overhead
Most of the time executor will go out of memory because of off-heap memory
What is stored in off-heap memory. --> what ever string you create as part of program, spark creates hash table of it, those are stored here.
Spark internal object are stored here, when ever we are using python or R all the object of those language will store here.
Off-heap memory is 10% of total memory assigned to executor memory.  

2. High concurrency:
 If we have disproportionate number of cores for executors, we will be processing too many partition. Each partition will have its metadata and memory overhead. Since they are running in parallel, they will be needing memory from executor and eventually cause OOM errors. To address this we can set the following configuration.
spark.default.parallelism
spark.executor.cores
While deciding on the number of executors keep in mind that, too few cores wont take advantage of multiple tasks running in executors (broadcast variables). Good place to start is with 5 executor-cores. You can enable dynamic resource allocation, but still you will need to decide on the number of cores per executor.


Or

For example, if a Hive ORC table has 2000 partitions, then 2000 tasks get created for the map stage for reading the table, assuming partition pruning did not come into play. If it’s a reduce stage (shuffle stage), then Spark will use either the spark.default.parallelism setting for RDDs or spark.sql.shuffle.partitions for data sets for determining the number of tasks. How many tasks are executed in parallel on each executor will depend on the spark.executor.cores property. If this value is set to a higher value without due consideration of the memory required, executors may fail with OOM. Now let’s see what happens under the hood while a task is getting executed and some probable causes of OOM.




3. Big partition: one of your partition is big
Let say you have one big partition on one machine and other machine working fine with executors but executor handling big partition cause problem, usually we will use parquet or orc format to store the file when ever executor tries to reading the data it will uncompress the data also, there may be so much of metadata created and there may be a so much of over head object get created while reading this partitions  which may cause out of memory 

Solution: make sure these partitions are appropriate 




Spark context vs Spark Session:
Spark context and spark session both are same, both are the entry point of spark programming, in spark 1.0 version we need explicitly create the context but in spark 2.0 version spark session
Includes the all the context. 

Its object sc is default available in spark-shell and it can be programmatically created using SparkContext class.

It’s object spark is default available in spark-shell and it can be created programmatically using SparkSession builder pattern.




Big Data Interview:
Sparks give you better performance than Hadoop.  Memory calculation 
Spark engine is different from Hadoop engine.
optimizing a job or optimizing a query (if a query is running long, how will you resolve it) Do you have any steps to resolve it.

How do you decide increase number of executors, before running job or while running job.

Hive query is running slow?
Need to check table is partitioned or not
Joins
Bucketing

Partition vs bucketing?

If we are getting a same file, then how partition will work?
What happening in the back-end when we are storing small files, Hadoop had lot of storage why can’t we store small files?


I have a table ID, name, AGE ( ID has unique value) we are doing partition on ID column than how?
Small files will be get created, I have one million unique records (one million small files will be get created).

Small file cause performance issue during reading the files. This cause overhead and slow down the overall processing time.

Resolve the small file issues:
Coalesce(10)
repartition()

df.cache()


Cardinality?

I have a table having huge data( 1million, high cardinality) I cannot use partition because it create multiple small file, how do you handle?
Bucketing will improve joining condition performance.

How do you merge your code and other team members code?

How do you schedule your  jobs?


Lets us say you have text file or csv, converting it into parquet or Avro, which file is good?

your writing data into a parquet file, what will happen in the backend?
If you need only one file, what will you do?

Coalesce will reduce the number of partition?


When you write file to hdfs, if the file size is greater than block size?


RDD:

RDD(Resilient Distributed Dataset):

Three ways to create RDDS:
		1. Parallelize
		2. from RDD using transformations
		3. Using external sources (HDFS, external or file system)
		
3. External Files:
rdd= sc.textFile("hdfs:///user/rajeshjkv5/NYSE_1997.txt.gz").map(lambda i:i.split(","))

RDD topics:
(https://runawayhorse001.github.io/LearningApacheSpark/rdd.html)


Transformations:
Essential core & Intermediate spark operations:
General                           Math/Statistical         Set Theory/ Relational               Data Structure / I/O

map                                sample                    union
filter                             randomsplit               intersection
flatMap          
mapPartitions
mapPartitionsWithIndex
groupBy
sortBy


Cartesian:
listA=[1,2,3,4]
listB= [5,6,7,8]
rdd1= sc.parallelize(listA)
rdd2= sc.parallelize(listB)
rdd1.cartesian(rdd2).collect()
[(1, 5), (1, 6), (1, 7), (1, 8), (2, 5), (2, 6), (2, 7), (2, 8), (3, 5), (3, 6), (3, 7), (3, 8), (4, 5), (4, 6), (4, 7), (4, 8)]




glom() Return an RDD created by coalescing all elements within each partition into an array.

CombineByKey():
groupByKey is Expensive
	Every single key value pair will be shuffled
	
combineByKey is one of optimisation 
more generic than aggregateByKey	


foreach():
def f(x):
...     print(x)
... 

fore=words.foreach(f)

akka
spark
scala
java
hadoop
pyspark
pyspark and spark
spark vs hadoop

groupByKey vs reduceByKey
Checkpointing



Key-value pair useful link(https://www.oreilly.com/library/view/learning-spark/9781449359034/ch04.html)





********  https://www.analyticsvidhya.com/blog/2016/10/using-pyspark-to-perform-transformations-and-actions-on-rdd/.       On RDD core concepts



Compression Ratio : GZIP compression uses more CPU resources than Snappy or LZO, but provides a higher compression ratio.

General Usage : GZip is often a good choice for cold data, which is accessed infrequently. Snappy or LZO are a better choice for hot data, which is accessed frequently.

Snappy often performs better than LZO. It is worth running tests to see if you detect a significant difference.

Splittablity : If you need your compressed data to be splittable, BZip2, LZO, and Snappy formats are splittable, but GZip is not.

GZIP compresses data 30% more as compared to Snappy and 2x more CPU when reading GZIP data compared to one that is consuming Snappy data.

LZO focus on decompression speed at low CPU usage and higher compression at the cost of more CPU.

For longer term/static storage, the GZip compression is still better.



ORC vs parquet: 
http://www.differencebetween.net/technology/difference-between-orc-and-parquet/

ORC, short for Optimized Row Columnar, is a free and open-source columnar storage format designed for Hadoop workloads
As the name suggests, ORC is a self-describing, optimized file format that stores data in columns which enables users to read and decompress just the pieces they need
It takes significantly less time to access data and also reduces the size of the data up to 75 percent

ORC provides many advantages over other Hive file formats such as high data compression, faster performance, 
predictive push down feature, and more over, the stored data is organized into stripes, which enable large, efficient reads from HDFS. 

Parquet:
Parquet is yet another open-source column-oriented file format in the Hadoop ecosystem backed by Cloudera, in collaboration with Twitter
Like ORC, Parquet provides columnar compressions saving you a great deal of storage space while allowing you to read individual columns 
instead of reading complete files.
It is more efficient at doing data IO style operations.
particularly designed keeping nested data structures in mind
Parquet is also a better file format in reducing storage costs and speeding up the reading step when it comes to large sets of data

ORC                                                                           parquet
ORC was inspired from the row columnar                          inspired from the nested data storage format outlined in the Google Dremel paper
format which was developed by Facebook                          and developed by Cloudera, in collaboration with Twitter.

ORC only supports Hive and Pig                                  While Parquet has a much broader range of support for the majority of the projects in the Hadoop ecosystem
                                                                Parquet works really well with Apache Spark


ORC files are organized into stripes of data, 
which are the basic building blocks for data and are independent of each other.
Each stripe has index, row data and footer.

                                                                 Parquet, on the other hand, stores data in pages and each page contains header information, 
                                                                 information about definition levels and repetition levels, and the actual data.
spark, hive vectorization:
columnar format is must for using vectorization.


Avro file format:
Apache Avro
Avro is a row-based storage format for Hadoop which is widely used as a serialization platform. 
Avro stores the data definition (schema) in JSON format making it easy to read and interpret by any program. 
The data itself is stored in binary format making it compact and efficient. 
A key feature of Avro is robust support for data schemas that change over time - schema evolution. 
Avro handles schema changes like missing fields, added fields and changed fields; as a result, 
old programs can read new data and new programs can read old data. 
This format is the ideal candidate for storing data in a data lake landing zone, because:

Data from the landing zone is usually read as a whole for further processing by downstream systems (the row-based format is more efficient in this case);

Downstream systems can easily retrieve table schemas from files (there is no need to store the schemas separately in an external meta store);

Avro data format successfully handles line breaks (\n) and other non-printable characters in data (for example, a string field can contain formatted JSON or XML file);

Any source schema change is easily handled (schema evolution).



Parquet vs avrò vs orc:
Parquet 
Column oriented storage format
Schema is store in the footer of the file
Due to merging of scheme cross multiple files, schema evolution is little expensive
Ideal for read heavy data operations
Excellent for selected column data consumption and processing
Works excellent with spark as there is vectorized reader for parquet

Partially split-ability
Most efficient to used in spark 

Avro:
Row oriented storage format
Schema is store as JSON within file
It is also a serialization and RPC framework
Excellent for schema evolution
Ideal for write heavy data operations
Excellent for entire row consumption and processing

Partially split-ability 
Most efficient to used in Kafka

ORC:
Column oriented storage format
Schema is store in the footer of the file schema evolution is limited to adding new columns
Ideal for read heavy data operations Excellent for selected column data consumption and processing
Works excellent with hive as there is vectorized reader for parquet

Partially split-ability 
Most efficient to used in Hive




Map vs flatmap:
Map:
 A map transformation is useful when we need to transform a RDD by applying a function to each element. So how can we use map transformation on ‘rdd’ in our case?

Flatmap:
The “flatMap” transformation will return a new RDD by first applying a function to all elements of this RDD, and then flattening the results.

Filter:
Where we can filter the data.

Please install psutil to have better support with spilling:
Spill here means writing the in-memory data frames to disk, which reduces the performance of pyspark, since writing to disk is slow.


groupBy:
 The “groupBy”  transformation will group the data in the original RDD. It creates a set of key value pairs, where the key is output of a user function, and the value is all items for which the function yields this key.

We have to pass a function (in this case, I am using a lambda function) inside the “groupBy” which will take the first 3 characters of each word in “rdd3”.
The key is the first 3 characters and value is all the words which start with these 3 characters.
After applying “groupBy” function, we store the transformed result in “rdd4” (RDDs are immutable – remember!). To view “rdd4”, we can print first (key, value) elements in “rdd4”.

rdd4 = rdd3.groupBy(lambda w: w[0:3])

print([(k, list(v)) for (k, v) in rdd3.take(1)])

Output: [(u'all', [u'all', u'allocates', u'all', u'all', u'allows', u'all', u'all', u'all', u'all', u'all', u'all', u'all'])]


Difference between groupByKey() and reduceByKey():

groupByKey() is just to group your dataset based on a key, all the key-value pairs are shuffled around. This is a lot of unnecessary data to being transferred over the network.
groupByKey can cause out of disk problems as data is sent over the network and collected on the reduce workers.

MyExplanation: Here, data is grouped based on keys and data is shuffled along the network which cause out of disk problems.

reduceByKey():
Data are combined at each partition, only one output for one key at each partition to send over the network. reduceByKey required combining all your values into another value with the exact same type.

MyExplanation: All the grouped data based on key, will be counted to a single value or reduced to a value for each key.
Data are combined at each partition, only one output for one key at each partition to send over the network 




mapPartitions:
It runs one at a time on each partition or block of the Rdd
mapPartitions() can be used as an alternative to map() and foreach() .
mapPartitions() can be called for each partitions while map() and foreach() is called for each elements
in an RDD


MappartionwithIndex():
It is similar to MapPartition but with one difference that it takes two parameters, the first parameter is the index and second is an iterator through all items within this partition


cogroup():
multiple pair rdd can be combined using cogroup().

ex: pair_rdd1, pair_rdd2
grouped= pair_rdd1.cogroup(pair_rdd2)


top():
Take highest value in the rdd

takeordered():
Take the least value in the rdd

myrdd1 = sc.parallelize(List(5,7,9,13,51,89)) myrdd1.top(3) 
//Array[Int]=Array(89,51,13) myrdd1.takeOrdered(3) 
//Array[Int] = Array(5, 7, 9) myrdd1.top(3) 
//Array[Int]=Array(89,51,13)


Explain the lookup() operation.?
> It is an action
> It returns the list of values in the RDD for key 'key'
Example:
val rdd1 = sc.parallelize(Seq(("myspark",78),("Hive",95),("spark",15),("HBase",25),("spark",39), ("BigData",78),("spark",49)))
rdd1.lookup("spark") rdd1.lookup("Hive") rdd1.lookup("BigData")
Output:
Seq[Int] = WrappedArray(15, 39, 49) Seq[Int] = WrappedArray(95) Seq[Int] = WrappedArray(78)


How to stop INFO messages displaying on spark console?
for Python: spark.sparkContext.setLogLevel("ERROR")





Union in rdd:
In Spark “union” transformation will return a new RDD by taking the union of two RDDs. Please note that duplicate items will not be removed in the new RDD


rdd3.getNumPartitions(). To get the number of partitions 


rdd3_coalesce = rdd3.coalesce(1). Rescue the number of partitions


mapPartitionsWithIndex(func):
Similar to mapPartitions, but also provides a function with an int value to indicate the index position of the partition.


Example:
>>> parallel = sc.parallelize(range(1,10),3)
>>> def show(index, iterator): yield 'index: '+str(index)+" values: "+ str(list(iterator))
>>> parallel.mapPartitionsWithIndex(show).collect()

['index: 0 values: [1, 2, 3]',
 'index: 1 values: [4, 5, 6]',
 'index: 2 values: [7, 8, 9]']

By using mappartitionswithindex will gives what the data store in the partitions based on index we will retrieve it.


** aggreagateByKey is same as reduceByKey but it takes initial values and combiner logic.


sortBy;



sortByKey:
Apache spark example:
br />
val rdd1 = sc.parallelize(Seq(("India",91),("USA",1),("Brazil",55),("Greece",30),("China",86),("Sweden",46),("Turkey",90),("Nepal",977)))<br />
val rdd2 = rdd1.sortByKey()<br />
rdd2.collect();<br />

* data will be sorted based on key, by default it true which means ascending order(small to big)
* dd1.sortByKey(false).  Descending oder( big to small)




Difference between orderBy and sortBy:
The ORDER BY clause is used to return the result rows in a sorted manner in the user specified order.

The SORT BY clause is used to return the result rows sorted within each partition in the user specified order. 
When there is more than one partition SORT BY may return result that is partially ordered



combinedbyKey:
http://www.hadoopexam.com/adi/index.php/spark-blog/90-how-combinebykey-works-in-spark-step-by-step-explaination


A key explanation from the second link is:

enter image description here

Let us see how combineByKey works in our use case. When combineByKey navigates through each element i.e for partition 1 - (Messi,45) it has a key which it has not seen before and when it moves to next (Messi,48) it gets a key which it has seen before. When it first time see a element , combineByKey() use function called createCombiner to create an initial value for the accumulator on that key. i.e. it use Messi as the key and 45 as value. So current value of the accumulator of that key (Messi) becomes 45. Now next time combineByKey() sees same key on same partition it does not use createCombiner instead it will make use of second function mergeValue with current value of accumulator (45) and new value 48.

Since all this happens parallel in different partition, there is chance that same key exist on other partition with other set of accumulators. So when results from different partition has to be merged it use mergeCombiners function.


Fold:
RDD. fold (zeroValue, op)[source] Aggregate the elements of each partition, and then the results for all the partitions, using a given associative function and a neutral “zero value.”



Lets me try to give simple examples to explain fold method of spark. I will be using pyspark here.

rdd1 = sc.parallelize(list([]),1)

Above line is going to create an empty rdd with one partition

rdd1.fold(10, lambda x,y:x+y)

This yield output as 20

rdd2 = sc.parallelize(list([1,2,3,4,5]),2)

Above line is going to create rdd with values 1 to 5 and will be having a total of 2 partitions

rdd2.fold(10, lambda x,y:x+y)

This yields output as 45

So in above case for sake of simplicity what is happening here is you are having zeroth element as 10. So the sum that you would otherwise get of all numbers in the RDD, is now added by 10(i.e. zeroth element+all other elements => 10+1+2+3+4+5 = 25). Also now we have two partitions(i.e. number of partitions*zeroth element => 2*10 = 20) Final output that fold emits is 25+20 = 45



foldByKey:

val a= spark.sparkContext.parallelize(Array(("a",1),("a",2),("b",2)))
val b =a.foldByKey(1)(_+_)

scala> b.collect
res2: Array[(String, Int)] = Array((b,3), (a,5)


(a,1) (a,2) => foldByKey(1)(_+_) => (a,1+1)+(a,2+1) => 2+3 = 5

(b,2) => foldByKey(1)(_+_) => (b,2+1) = 3




foldByKey(zeroValue, func, numPartitions=None, partitionFunc=<function portable_hash>)[source]¶
Merge the values for each key using an associative function “func” and a neutral “zeroValue” which may be added to the result an arbitrary number of times, and must not change the result (e.g., 0 for addition, or 1 for multiplication.).

Examples

>>>
rdd = sc.parallelize([("a", 1), ("b", 1), ("a", 1)])
from operator import add
sorted(rdd.foldByKey(0, add).collect())
[('a', 2), ('b', 1)]


countByKey()
Through countByKey operation, we can count the number of elements for each key.
rdd.countByKey()


Histogram:
PySpark Histogram is a way in PySpark to represent the data frames into numerical data by binding the data with possible aggregation functions. 
It is a visualisation technique that is used to visualise the distribution of variable


Pair RDD:
RDDs, which contains the key/value pairs are called as pair RDDs.
Pair RDD will work on key based concepts
Like aggregateByKey, combineByKey, groupByKey, reduceByKey ....  Pair RDD transformations

Pair RDD actions:
countByKey, collectAsMap, lookup, saveAsHadoopDataset.

https://sparkbyexamples.com/apache-spark-rdd/spark-pair-rdd-functions/. 

Types of Partition in RDD:
HashPartition:
It uses the hashcode() method to determine the partition in spark.
So based on this hashcode() concept, HashPartitioner will divide the keys that have the same hash code().

Partition = key.hashcode() % numPartitions

Range Partition:
Define a range on a partition.



Data is spread in all the nodes of cluster, how spark tries to process this data?
By default, spark tries to read data into an RDD from the nodes that are close to it. To optimise transformation operations spark creates partitions to hold the data chunks.

What is shuffling:
Shuffling is a process of repartitioning data across partitions and may cause moving it across JVMS or even network when it is redistributed among executors.

What is checkpointing?

Checkpointing is a process of truncating RDD lineage graph and saving it to HDFS. RDD checkpointing saves the actual intermediate RDD data to a reliable distributed file system.

When running spark applications, it is necessary to install spark on all the nodes of a cluster.
Spark need not be installed when running a job under YARN or MESOS because spark can execute on top of YARN or MESOS cluster without effecting any changes to the cluster.


Can you trigger automatic clean-ups in spark to handle accumulated metadata?
Spark.cleaner.ttl


By default how many partitions are created in RDD in apache spark?
No of cores in a cluster = no of partitions

Date function in spark:
current_date
current_timestamp
Day
DayofMonth
To_date
Date_add
Date_sub


from pyspark.sql.functions import unix_timestamp, from_unixtime

df = spark.createDataFrame(
    [("11/25/1991",), ("11/24/1991",), ("11/30/1991",)], 
    ['date_str']
)

df2 = df.select(
    'date_str', 
    from_unixtime(unix_timestamp('date_str', 'MM/dd/yyy')).alias('date')
)

print(df2)
#DataFrame[date_str: string, date: timestamp]

df2.show(truncate=False)
#+----------+-------------------+
#|date_str  |date               |
#+----------+-------------------+
#|11/25/1991|1991-11-25 00:00:00|
#|11/24/1991|1991-11-24 00:00:00|
#|11/30/1991|1991-11-30 00:00:00|
#+----------+-------------------+











Spark/PySpark Deploy Modes
There are two deploy modes that the Standalone cluster manager offers for where the driver program of an application can execute. They are:
Client Mode (Default Mode): In this mode, the driver will be launched on that machine where the spark-submit command was executed. 
 Cluster Mode: In this mode, the driver will run inside the Standalone cluster as another procedure on one of the worker nodes, and after that, it will link back to request executors.



Read and write option in all the files:

df= spark.read
.option("header", True)
.option("inferSchema",True) 
.option("delimiter",",")
.option("multiline", True) --json data




df = spark.read.format("jdbc").options(url=url_rq, driver=driver_rq, dbtable=sql_rq, "username"=username_rq, "password"=passkey_rq).load()

.option("charset", "UTF-8")
.option("mode", "DROPMALFORMED")



header=True, 
multiLine=True, 
ignoreLeadingWhiteSpace=True, 
ignoreTrailingWhiteSpace=True, 
encoding="UTF-8",
sep=',',
quote='"', 
escape='"',
maxColumns=2,
inferSchema=True
"timestampFormat" -> "yyyy-MM-dd HH:mm:ss.SSSZZZ",


-- https://spark.apache.org/docs/latest/sql-data-sources-csv.html.  in this link we find all option while reading/writing for each file format.




All Topics:

'SELECT', 'FROM', 'ADD', 'AS', 'ALL', 'ANY', 'DISTINCT', 'WHERE', 'GROUP', 'BY', 'GROUPING', 'SETS', 'CUBE', 'ROLLUP', 'ORDER', 'HAVING', 'LIMIT', 'AT', 'OR', 'AND', 'IN', NOT, 'NO', 'EXISTS', 'BETWEEN', 'LIKE', RLIKE, 'IS', 'NULL', 'TRUE', 'FALSE', 'NULLS', 'ASC', 'DESC', 'FOR', 'INTERVAL', 'CASE', 'WHEN', 'THEN', 'ELSE', 'END', 'JOIN', 'CROSS', 'OUTER', 'INNER', 'LEFT', 'SEMI', 'RIGHT', 'FULL', 'NATURAL', 'ON', 'PIVOT', 'LATERAL', 'WINDOW', 'OVER', 'PARTITION', 'RANGE', 'ROWS', 'UNBOUNDED', 'PRECEDING', 'FOLLOWING', 'CURRENT', 'FIRST', 'AFTER', 'LAST', 'ROW', 'WITH', 'VALUES', 'CREATE', 'TABLE', 'DIRECTORY', 'VIEW', 'REPLACE', 'INSERT', 'DELETE', 'INTO', 'DESCRIBE', 'EXPLAIN', 'FORMAT', 'LOGICAL', 'CODEGEN', 'COST', 'CAST', 'SHOW', 'TABLES', 'COLUMNS', 'COLUMN', 'USE', 'PARTITIONS', 'FUNCTIONS', 'DROP', 'UNION', 'EXCEPT', 'MINUS', 'INTERSECT', 'TO', 'TABLESAMPLE', 'STRATIFY', 'ALTER', 'RENAME', 'ARRAY', 'MAP', 'STRUCT', 'COMMENT', 'SET', 'RESET', 'DATA', 'START', 'TRANSACTION', 'COMMIT', 'ROLLBACK', 'MACRO', 'IGNORE', 'BOTH', 'LEADING', 'TRAILING', 'IF', 'POSITION', 'EXTRACT', 'DIV', 'PERCENT', 'BUCKET', 'OUT', 'OF', 'SORT', 'CLUSTER', 'DISTRIBUTE', 'OVERWRITE', 'TRANSFORM', 'REDUCE', 'SERDE', 'SERDEPROPERTIES', 'RECORDREADER', 'RECORDWRITER', 'DELIMITED', 'FIELDS', 'TERMINATED', 'COLLECTION', 'ITEMS', 'KEYS', 'ESCAPED', 'LINES', 'SEPARATED', 'FUNCTION', 'EXTENDED', 'REFRESH', 'CLEAR', 'CACHE', 'UNCACHE', 'LAZY', 'FORMATTED', 'GLOBAL', TEMPORARY, 'OPTIONS', 'UNSET', 'TBLPROPERTIES', 'DBPROPERTIES', 'BUCKETS', 'SKEWED', 'STORED', 'DIRECTORIES', 'LOCATION', 'EXCHANGE', 'ARCHIVE', 'UNARCHIVE', 'FILEFORMAT', 'TOUCH', 'COMPACT', 'CONCATENATE', 'CHANGE', 'CASCADE', 'RESTRICT', 'CLUSTERED', 'SORTED', 'PURGE', 'INPUTFORMAT', 'OUTPUTFORMAT', DATABASE, DATABASES, 'DFS', 'TRUNCATE', 'ANALYZE', 'COMPUTE', 'LIST', 'STATISTICS', 'PARTITIONED', 'EXTERNAL', 'DEFINED', 'REVOKE', 'GRANT', 'LOCK', 'UNLOCK', 'MSCK', 'REPAIR', 'RECOVER', 'EXPORT', 'IMPORT', 'LOAD', 'ROLE', 'ROLES', 'COMPACTIONS', 'PRINCIPALS', 'TRANSACTIONS', 'INDEX', 'INDEXES', 'LOCKS', 'OPTION', 'ANTI', 'LOCAL', 'INPATH', IDENTIFIER, BACKQUOTED_IDENTIFIER



spark sql: (pyspark sql)

Below all are converting dataframe data into table(view) format.
spark sql will work with table format only.
 
createGlobalTempView(name) -- Creates a global temporary view with this DataFrame. The lifetime of this temporary view is tied to this Spark application. 
createOrReplaceGlobalTempView(name)  -- Creates or replaces a global temporary view using the given name. The lifetime of this temporary view is tied to this Spark application.
createTempView(name)   -- Creates a local temporary view with this DataFrame. The lifetime of this temporary table is tied to the SparkSession that was used to create this DataFrame. throws TempTableAlreadyExistsException, if the view name already exists in the catalog.
createOrReplaceTempView(name)  -- Creates or replaces a local temporary view with this DataFrame. The lifetime of this temporary table is tied to the SparkSession that was used to create this DataFrame.


Dataframe to sparksql:
registerDataFrameAsTable(df, "table1")  deprecated 
registerTempTable()  deprecated


query:
df2= spark.sql("select * from temp_table")
or 
spark.table("temp_table").show()


queries:
spark.sql("""/
                           SELECT
                             protocol_type,
                             CASE label
                               WHEN 'normal.' THEN 'no attack'
                               ELSE 'attack'
                             END AS state,
                             COUNT(*) as total_freq,
                             ROUND(AVG(src_bytes), 2) as mean_src_bytes,
                             ROUND(AVG(dst_bytes), 2) as mean_dst_bytes,
                             ROUND(AVG(duration), 2) as mean_duration,
                             SUM(num_failed_logins) as total_failed_logins,
                             SUM(num_compromised) as total_compromised,
                             SUM(num_file_creations) as total_file_creations,
                             SUM(su_attempted) as total_root_attempts,
                             SUM(num_root) as total_root_acceses
                           FROM connections
                           GROUP BY protocol_type, state
                           ORDER BY 3 DESC
                           """)
                           
                           
                           
 tcp_attack_stats = spark.sql("""
                                   SELECT
                                     service,
                                     label as attack_type,
                                     COUNT(*) as total_freq,
                                     ROUND(AVG(duration), 2) as mean_duration,
                                     SUM(num_failed_logins) as total_failed_logins,
                                     SUM(num_file_creations) as total_file_creations,
                                     SUM(su_attempted) as total_root_attempts,
                                     SUM(num_root) as total_root_acceses
                                   FROM connections
                                   WHERE protocol_type = 'tcp'
                                   AND label != 'normal.'
                                   GROUP BY service, attack_type
                                   ORDER BY total_freq DESC
                                   """)
tcp_attack_stats.show()







tcp_attack_stats = spark.sql("""
                                   SELECT
                                     service,
                                     label as attack_type,
                                     COUNT(*) as total_freq,
                                     ROUND(AVG(duration), 2) as mean_duration,
                                     SUM(num_failed_logins) as total_failed_logins,
                                     SUM(num_file_creations) as total_file_creations,
                                     SUM(su_attempted) as total_root_attempts,
                                     SUM(num_root) as total_root_acceses
                                   FROM connections
                                   WHERE (protocol_type = 'tcp'
                                          AND label != 'normal.')
                                   GROUP BY service, attack_type
                                   HAVING (mean_duration >= 50
                                           AND total_file_creations >= 5
                                           AND total_root_acceses >= 1)
                                   ORDER BY total_freq DESC
                                   """)
tcp_attack_stats.show()





tcp_attack_stats = spark.sql("""
                                   SELECT
                                     t.service,
                                     t.attack_type,
                                     t.total_freq
                                   FROM
                                   (SELECT
                                     service,
                                     label as attack_type,
                                     COUNT(*) as total_freq,
                                     ROUND(AVG(duration), 2) as mean_duration,
                                     SUM(num_failed_logins) as total_failed_logins,
                                     SUM(num_file_creations) as total_file_creations,
                                     SUM(su_attempted) as total_root_attempts,
                                     SUM(num_root) as total_root_acceses
                                   FROM connections
                                   WHERE protocol_type = 'tcp'
                                   AND label != 'normal.'
                                   GROUP BY service, attack_type
                                   ORDER BY total_freq DESC) as t
                                     WHERE t.mean_duration > 0
                                   """)
tcp_attack_stats.show()              



bucketing in pyspark sql:
https://luminousmen.com/post/the-5-minute-guide-to-using-bucketing-in-pyspark


The Bucketing is commonly used to optimize performance of a join query by avoiding shuffles of tables participating in the join. 
Bucketing can benefit when pre-shuffled bucketed tables are used more than once in the query.         





imp:

from pyspark.conf import SparkConf
from pyspark.context import SparkContext
from pyspark.sql import HiveContext

sc= SparkContext('local','example')
hc = HiveContext(sc)
tf1 = sc.textFile("hdfs://cdhstltest/user/data/demo.CSV")
print(tf1.first())

hc.sql("use intg_cme_w")
spf = hc.sql("SELE		


*****
dropna()  or df.na.drop()  Vs  fillna()
Dropna(how="any") -- will drop all the null values from rows and columns
Dropna(how="all") -- drop all the null values from particular row or particular column
df.dropna(subset="City")  --particular column nulls will be dropped


fillna(0) or df.na.fill(0) --- null is replace by 0

dropDuplicate()
 


Clear screen:
import os
os.system('clear')


Change the columns order.
f2=df1.select(sorted(df1.columns))
df2.show()


Connect to S3 from pyspark:
https://medium.com/@sivachaitanya/accessing-aws-s3-from-pyspark-standalone-cluster-6ef0580e3c08
https://towardsai.net/p/programming/pyspark-aws-s3-read-write-operations


Column conversion or data type conversion:
pvdf_new=pvdf.withColumn("Year", col("1990").cast(IntegerType()))
pvdf_new2=pvdf.select(col("1990").cast("int").alias("ABC"))



Pivot:  (when working with pivot groupBy and aggregation is mandatory.
 df2=df.groupBy("Product").pivot("Country").sum("Amount")
 pvdf_new.groupBy("Name").pivot("1990").sum("year").show()


----- connect to external database:

mysql installation and commands in command line interface
export path into bash_profile

mysql --user=root -p
password:


spark=SparkSession.builder.appName("Demo").config("sparks.jars", "file:///Users/rajeshjakkula/Downloads/mysql-connector-java-5.1.46/mysql-connector-java-5.1.46.jar")
.config("spark.executor.extraClassPath", "file:///Users/rajeshjakkula/Downloads/mysql-connector-java-5.1.46/mysql-connector-java-5.1.46.jar")
.config("park.executor.extraLibrary", "file:///Users/rajeshjakkula/Downloads/mysql-connector-java-5.1.46/mysql-connector-java-5.1.46.jar")
.config("spark.driver.extraClassPath", "file:///Users/rajeshjakkula/Downloads/mysql-connector-java-5.1.46/mysql-connector-java-5.1.46.jar")
.enableHiveSupport()
.getOrCreate()


url_rq="jdbc:mysql://localhost:3306/mysql"
driver_rq="com.mysql.jdbc.Driver"
username_rq="root"
passkey_rq="mokshith1@A"
sql_rq= """(select * from "+table_name + ") as sample"""


df = spark.read.format("jdbc").options(url=url_rq, driver=driver_rq, dbtable=sql_rq, "username"=username_rq, "password"=passkey_rq).load()

mysql connect java jar file path in mylocal
/Users/rajeshjakkula/Downloads/mysql-connector-java-5.1.46/mysql-connector-java-5.1.46.jar





Left semi vs left anti:

Left anti is opposite to left outer join, all the not matching data from left table is return.

Left semi join is quite similar to inner join only the difference is all the columns from left table will only be return, right table columns are not returned.

Example:

TabA         TabB
Id Lett    Id  Let
3  A       3   E
4  B       4   F

Select * from tabA aa inner join tabB bb on aa.id=bb.id

Result set:
Id  Lett  Id  Let
3   A    3    E
4   B    4    F

Select * from tabA aa leftsemi join tabB bb on aa.id=bb.id

Result set:
Id   Lett  
3    A   
4    B   

Here the difference is right table columns are not returned in the result set.




%sql
CREATE TABLE department( deptId Int, Name String)
  USING DELTA
  LOCATION '/mnt/delta/aldsdataplace'


df=spark.read.format("csv").option("header", "true").load("dbfs:/FileStore/tables/employee_4.csv")

display(df)

df2=df.select("empid", "Name")
df2.show()

from pyspark.sql.functions import *
df2.filter(col('empid')==100).show()

table_name='department'


df.write.format("parquet").mode("overwrite").saveAsTable(table_name)


/mnt/delta/aldsdataplace




inferSchema:
inferSchema -> Infer schema will automatically guess the data types for each field. If we set this option to TRUE, 
the API will read some sample records from the file to infer the schema. If we want to set this value to false, we must specify a schema explicitly


df=spark.read.format("csv").option("inferSchema", "true").option("header","true").load(srcloc)
display(df)


MergeSchema:
Let say we have create few dataframe in the middle with different data types and end, we are combining all the dataframe to a single dataframe.
Here we may get schema mismatch during writing a dataframe or read a dataframe once it write. 

To overcome this problem we will be using mergeSchema during the write operation.


df4.write.format("delta").mode("append").option("mergeSchema", "true").save(deltaPath)

Ref: https://mungingdata.com/delta-lake/schema-enforcement-evolution-mergeschema-overwriteschema/


Failed to merge incompatible data type float type and double type
Facing any issue on datatype compatibility
At writing   .option(“overwriteSchema”, “true”)

----------------------------------------


Reading a excel file:

Reading excel xlsx file in Pyspark Databricks:
We can’t read a xlsx file directly, we have to install a libraries in the cluster
com.crealytics:spark-excel_2.12:0.13.5



sample1DF = spark.read.format(“com.crealytics.spark.excel”) .option(“header”, “true”).option(“inferSchema”, “true”).load(“path”)




Checking a column has integer values or not:
If a column has integer it return true, if not return false

from pyspark.sql import functions as F

my_df.select(
  "ID",
  F.col("ID").cast("int").isNotNull().alias("Value ")
).show()

+-----+------+
|   ID|Value |
+-----+------+
|25q36| false|
|75647|  true|
|13864|  true|
|8758K| false|
|07645|  true|
+-----+------+



Finding a length in dataframes:

from pyspark.sql.functions  import *
df.select("empid", length(col("empid")).alias("length")).show()



* Dataframe itself we don’t have subquery or correlated query concept
But in spark.sql we had it and in data bricks %sql we have subquery and correlated query concept.





** size and shape in pyspark dataframe means count and length.


** df.dtypes.      finding data type in data frame level


Multiple when condition and using or, and in between
from pyspark.sql import functions as F

df=df.withColumn('new_column', 
    F.when(F.col('fruit1')==F.col('fruit2'), 1)
    .otherwise(F.when((F.col('fruit1').isNull()) | (F.col('fruit2').isNull()), 3))
    .otherwise(0))
 

Or 

dataDF.withColumn("new_column",
       when((col("code") == "a") | (col("code") == "d"), "A")
      .when((col("code") == "b") & (col("amt") == "4"), "B")
      .otherwise("A1")).show()



** run python script in pyspark shell:
./bin/spark-submit mypythonfile.py








Custom User-defined Functions(UDF):

UDF’s a.k.a User Defined Functions, If you are coming from SQL background, UDF’s are nothing new to you as most of the traditional RDBMS databases support User Defined Functions, these functions need to register in the database library and use them on SQL as regular functions.

Our code will be register as custom defined function:
 def total_salary(sal, comm):
 	if comm is None:
 		return sal
 	else:
 		return sal+comm


ID,SAL,COMM, SAL_COMM
1,100,10,110
2,200,null, 200
3,300,null,300

our user defined function will return if comm is null then salary otherwise sal+comm



UDF at spark sql:
from pyspark.sql.types import IntergerType

spark.udf.register(name='total_salary', f=total_salary, returnType=IntergerType())

 *This user defined function store in sql metastore.



 * read a csv file and registeras view
 and select statement



 select col1, col2, total_salary(sal, comm) as sum from view.

 This UDF need to executed in this note only or session only.


UDF at dataframe:
from pyspark.sql.functions import udf
from pyspark.sql.types import LongType
squared_udf = udf(total_salary, IntegerType())
df = spark.table("test")
display(df.select("id", total_salary(“id").alias("id_squared")))



UDF can done using annotation as well:
from pyspark.sql.functions import udf
@udf("long")
def squared_udf(s):
  return s * s
df = spark.table("test")
display(df.select("id", squared_udf("id").alias("id_squared")))


 or


 
    def extract_tags(word):

        if word.lower().startswith("#"):
            return word
        else:
            return "nonTag"

    extract_tags_udf = udf(extract_tags , StringType())

    resultDF = words.withColumn("tags", extract_tags_udf(words.word))




Simple example:
Def squared(s):
	return s*s
spark.udf.register("squaredwithpython", squared)


Optinal return type will also mention.
From pyspark.sql.functions import LongType()
Def squared(s):
	return s*s
spark.udf.register("squaredwithpython", squared, LongType())

Calling UDF from spark sql
%sql
Select id, squaredwithpython(id) as is_suared from table.




2.How can you minimize data transfers when working with Spark?

Minimizing data transfers and avoiding shuffling helps write spark programs that run in a fast and reliable manner. The various ways in which data transfers can be minimized when working with Apache Spark are:

Using Broadcast Variable- Broadcast variable enhances the efficiency of joins between small and large RDDs.
Using Accumulators – Accumulators help update the values of variables in parallel while executing.
The most common way is to avoid operations ByKey, repartition or any other operations which trigger shuffles.

3.  How can you trigger automatic clean-ups in Spark to handle accumulated metadata?

You can trigger the clean-ups by setting the parameter ‘spark.cleaner.ttl’ or by dividing the long running jobs into different batches and writing the intermediary results to the disk


5. Explain about the different types of transformations on DStreams?

Stateless Transformations- Processing of the batch does not depend on the output of the previous batch. Examples – map (), reduceByKey (), filter ().
Stateful Transformations- Processing of the batch depends on the intermediary results of the previous batch. Examples –Transformations that depend on sliding windows.


6. What is Spark Core?

It has all the basic functionalities of Spark, like - memory management, fault recovery, interacting with storage systems, scheduling tasks, etc.

7. Explain the difference between Spark SQL and Hive.

Spark SQL is faster than Hive.
Any Hive query can easily be executed in Spark SQL but vice-versa is not true.
Spark SQL is a library whereas Hive is a framework.
It is not mandatory to create a metastore in Spark SQL but it is mandatory to create a Hive metastore.
Spark SQL automatically infers the schema whereas in Hive schema needs to be explicitly declared.


8. What are scalar and aggregate functions in Spark SQL?

In Spark SQL, Scalar functions are those functions that return a single value for each row. Scalar functions include built-in functions including array functions and map functions. Aggregate functions return a single value for a group of rows. Some of the built-in aggregate functions include min(), max(), count(), countDistinct(), avg(). Users can also create their own scalar and aggregate functions.


Shared variables:
Shared variable are nothing but broadcast variable and accumulator.



Refresh table in Pyspark:
Invalidates and refreshes all the cached data and metadata of the given table. 
For performance reasons, Spark SQL or the external data source library it uses might cache certain metadata about a table, such as the location of blocks. 
When those change outside of Spark SQL, users should call this function to invalidate the cache.
spark.catalog.refreshTable("student3")

spark.catalog.refreshTable("student3")




Pyspark update: (how to modify one column value in one row used by pyspark)
There is no direct update statement in pyspark, 


Use the below code to update on single column level 

df.withColumn("State", when(col("Zipcode")==704, valueTrue).otherwise(col("State"))).show()

+-------------------+------------+-----+-----------+-------+
|               City|RecordNumber|State|ZipCodeType|Zipcode|
+-------------------+------------+-----+-----------+-------+
|PASEO COSTA DEL SUR|           2|   PR|   STANDARD|    704|
|       BDA SAN LUIS|          10|   PR|   STANDARD|    709|
+-------------------+------------+-----+-----------+-------+


+-------------------+------------+-----+-----------+-------+
|               City|RecordNumber|State|ZipCodeType|Zipcode|
+-------------------+------------+-----+-----------+-------+
|PASEO COSTA DEL SUR|           2| null|   STANDARD|    704|
|       BDA SAN LUIS|          10|   PR|   STANDARD|    709|
+-------------------+------------+-----+-----------+-------+




Delete in pyspark:
There is specific delete function in pyspark, we can use drop to delete the column( entire column will be dropped).

df.drop(“col1”)
df.drop(“col2”, “col3”)


If we want to drop entire table with in the data frame level, then

list = ['Employee ID','Employee NAME','Company Name']
  
# delete two columns
dataframe = dataframe.drop(*list)


If you want to delete or remove specific row, we can’t do it simple like ( delete from table where id=2 in oracle)
Here we have remove or not select that particular records and create a new data frame.

*note in pyspark dataframe, spark.sql
df.show()
+-------------------+------------+-----+-----------+-------+
|               City|RecordNumber|State|ZipCodeType|Zipcode|
+-------------------+------------+-----+-----------+-------+
|PASEO COSTA DEL SUR|           2|   PR|   STANDARD|    704|
|       BDA SAN LUIS|          10|   PR|   STANDARD|    709|
+-------------------+------------+-----+-----------+-------+

df2=df.where("Zipcode <>  '704'")
df2.show()
+------------+------------+-----+-----------+-------+
|        City|RecordNumber|State|ZipCodeType|Zipcode|
+------------+------------+-----+-----------+-------+
|BDA SAN LUIS|          10|   PR|   STANDARD|    709|
+------------+------------+-----+-----------+-------+




Slots:
"Slots" is a term Databricks uses (or used?) for the threads available to do parallel work for Spark. 
The Spark documentation and Spark UI calls the same concept "cores", even though they are unrelated to physical CPU cores




Sort vs order by:
sort() is more efficient compared to orderBy() because the data is sorted on each partition individually and this is why the order in the output data is not guaranteed. 
On the other hand, orderBy() collects all the data into a single executor and then sorts them.


They are NOT the SAME.

The SORT BY clause is used to return the result rows sorted within each partition in the user specified order. When there is more than one partition SORT BY may return result that is partially ordered.


The ORDER BY clause is used to return the result rows in a sorted manner in the user specified order. Unlike the SORT BY clause, this clause guarantees a total order in the output.



Union vs union ALL:
DataFrame unionAll() – unionAll() is deprecated since Spark “2.0. 0” version and replaced with union(). 
Note: In other SQL's, Union eliminates the duplicates but UnionAll combines two datasets including duplicate records. 
But, in spark both behave the same and use DataFrame duplicate function to remove duplicate rows



lower(col('state_name'))
upper(col('state_name'))



---------------
To view the table info:

DESCRIBE DETAIL

DESCRIBE HISTORY


---------------------------
Read a delta table from adls account:

df1 = spark.read.format("delta") \
  .option("fs.azure.account.key.<storage-account-name>.dfs.core.windows.net", "<storage-account-access-key-1>") \
  .read("...")
df2 = spark.read.format("delta") \
  .option("fs.azure.account.key.<storage-account-name>.dfs.core.windows.net", "<storage-account-access-key-2>") \
  .read("...")
df1.union(df2).write.format("delta") \
  .mode("overwrite") \
  .option("fs.azure.account.key.<storage-account-name>.dfs.core.windows.net", "<storage-account-access-key-3>") \
  .save("...")









Practise problems:
If you using windows analytical functions import should be proper
from pyspark.sql.functions import * (col)
from pyspark.sql.window import * (partitionBy, over)
from pyspark.sql.window import Window 
from pyspark.sql.functions import rank



Big data processing framework:
Batch only --> Apache Hadoop (hdfs, yarn, map reduce)
Stream only --> Apache storm(streams, spouts, bolts), Apache samza (Kafka, yarn, samza api) 
Hybrid  --> Apache Spark(Mlib, Spark SQL, graphs, spark streaming, spark core), Apache Flink (Data Stream API, Dataset API, Table API, Gellt, Flink ML).








** If we are trying to write file again with out change in code then file will be place in the target path (not new file will be place).



** skewness:
When the data are not balanced between workers, we call the data “skewed.”

Data is not evenly distributed in the partition is called skewness.

To fix this issue, data need to be distributed evenly in all the partitions.

Using repartition issue can be fixed
Using Salting technique issue can be fixed.  Spark 2.0
Using adaptive query execution from spark 3.o onwards. (https://www.youtube.com/watch?v=PiZcQKbomDU)
Spark.conf.set("spark.sql.adaptive.enabled", "true" once you enabled this option in spark, with same joining condition skewness can be get rid off. (Not face skewness)




Salt:
If you’re not sure what columns would lead to even workload by your app, 
you can use a random salt to evenly distribute data across cores. 
All we do is create a column with a random value the partition by that column


import pyspark.sql.functions as F
df = df.withColumn('salt', F.rand())
df = df.repartition(8, 'salt')
To check if our salt worked, we can use the same groupBy as above…

df.groupBy(F.spark_partition_id()).count().show()

Image:
SPARK_PARTITION_ID() count
0 130
1 103
2 143
3 125
4 111
5 128
6 147
7 113

Reference:
https://towardsdatascience.com/data-skew-in-pyspark-783d529a9dd7


To view the partitions and data:
import pyspark.sql.functions as F
df.groupBy(F.spark_partition_id()).count().show()


df.rdd.glom().collect()


Refer this link for the skewness.... https://itnext.io/handling-data-skew-in-apache-spark-9f56343e58e8

https://docs.databricks.com/optimizations/skew-join.html. skewness join optimization.



What is the meaning of data profiling?
Data profiling is a technology for discovering and investigating data quality issues, such as duplication, lack of consistency, and lack of accuracy and completeness.

Data Quality checks:

source, target data validation (count, filtered records..), null checks, length check, space check.


Data cleaning:
Here are 8 effective data cleaning techniques:

Remove duplicates
Remove irrelevant data
Standardize capitalization
Convert data type
Clear formatting
Fix errors
Language translation
Handle missing values




Spark catalog:
Catalog is the interface for managing a metastore (aka metadata catalog) of relational entities (e.g. database(s), tables, functions, table columns and temporary views).

Metadata such as table names, column names, data types etc for the permanent tables or views will be stored in Metastore. We can access the metadata using spark.catalog which is exposed as part of spark session object.


Accessing:
Spark.catalog

help(spark.catalog)


spark.catalog.listDatabases()
Spark.catalog.listTables(passdatabasenameasargument)
spark.catalog.listColumns(tables name, database name)



Def tablename():
list=[]
	for db in spark.catalog.listDatabases():
		for table in Spark.catalog.listTables(db.name)
			for columns in spark.catalog.listColumns(table.name, database.name)

List.append([db.name, tables.name, columns.name])
Return list

df=spark.createdataframe(tablename(), ["db_name, table_name, column_name"])
display(df). 
 Above code will do, get all the database, table and column and create a dataframe.

Catalog functions:
cacheTable
clearCache
createTable
currentDatabase
dropTempView
listColumns.     etc....

https://jaceklaskowski.gitbooks.io/mastering-spark-sql/content/spark-sql-Catalog.html


Upgrading hive metastore into catalog will help in built-in auditing and access control.



To know list of dataframe in the session or notebook:
print([k for (k,v) in globals().items() if is instance(v, DataFrame)])
It print all dataframes means df, sdf, df1, df2....



input_file_name:

From pyspark.sql.functions import input_file_name
Let us say you have 10 csv files you want to know which records belongs to which file after writing into target.

Using this input_file_name function we can write all file path into that particular file record.

From pyspark.sql.functions import input_file_name 
df=spark.read.csv("path", header=True)
display(df.withColumn("filename", input_file_name() ))

To know count on each file level
From pyspark.sql.functions import input_file_name 
df=spark.read.csv("path", header=True)
display(df.withColumn("filename", input_file_name() )).groupby("file_name").count()


How to add partition_id to dataframe.
From pyspark.sql.functions import spark_partition_id 
df=spark.read.csv("path", header=True)
display(df.withColumn("partitioned", spark_partition_id() ))


Partitionwise number of records::
From pyspark.sql.functions import spark_partition_id 
df=spark.read.csv("path", header=True)
display(df.withColumn("partitionid", spark_partition_id() )).groupby("partitionid").count()



If you want to maintain a sequence to data without changing sequence.
Let say, using monotonically_increasing_id()we can assign a sequence  but accidentally we have deleted the data and again try to assign a key to same data but there sequence will change.
To remain same sequence to same data we use MD5 and sha2

Display(df.withColumn("key", MD5("empno")))     --> empno is the column in table and we can keep n number of column in the MD5
Similar for sha2

Display(df.withColumn("key", sha2("empno"), 256)) 




RecursiveFileLookup: how read all files from nested folder in pySpark dataframe
If a folder(main folder) contains subfolders and files in the main folder and subfolder. To read data from all how in Pyspark dataframe?

Using recursivefilelookup

main_folder (customerfile.csv) --> 2022 (customerfile2.csv) --> 2021 (customerfile3.csv)

df1=spark.read.format("csv").option("recursiveFileLookup", "true").load("path")





* optiv:

When we are connecting to external source only one executors is running among of 10 because.
External database, hitting API and csv file, if our source is among three of them then it read on only one thread.
Write into a file and process further then we have partition and executors run.

* Data is stored in file because of this issue,  filed data can be process fast and we can do partition, set using of all executors......
Data Is not store in database.


---------------------------------------------------------------------------------------------------------------------------------


Data Locality and Apache Spark
**********************************

Have you ever noticed the term "NODE_LOCAL" or "RACK_LOCAL" as in picture below While analyzing and debugging spark job issues/behavior using spark UI ? Have you ever heard the term data locality ?
 
Data locality is a concept that is used in many distributed computing frameworks and MPP engines(not just Spark). The basic idea of data locality is to co-locate computation with data, in order to minimize the amount of data that needs to be transferred over the network.
 
The LocalityPreferredContainerPlacementStrategy is a feature of Apache Spark that determines how the framework decides where to place tasks within a cluster. Specifically, it is a scheduling strategy that tries to schedule tasks on the same node where the data they require is already stored. This is known as data locality, and it can lead to significant performance gains by reducing the amount of data that needs to be transferred across the network.
 
When Spark receives a task to be executed, it checks whether the required data is available in memory on any node in the cluster. If so, it assigns the task to that node, even if there are other nodes with more available resources. This is because accessing data from memory is faster than fetching it over the network.
 
It Checks for data locality in below order of localities:

>> PROCESS_LOCAL: This is the highest locality level, where the task is executed on the same JVM (Java Virtual Machine) process as the data. This level of locality is achieved when the data is already present in the memory of the executor where the task is scheduled. In this case, no data transfer is required over the network.
 
>> NODE_LOCAL: This level of locality is achieved when the data is available on the same node where the task is scheduled to run. In this case, the data transfer is required over the network, but it happens within the same node, which is much faster than transferring data across different nodes.

>> RACK_LOCAL: This locality level is achieved when the data is present on a different node, but on the same rack as the node where the task is scheduled to run. In this case, the data transfer happens across different nodes but within the same rack, which is faster than transferring data across different racks.

>> ANY : Here , the task can run on any node, regardless of the data location. This level of locality is used when there is no data locality information available or when the data is not available in the memory of any executor. The data transfer in this case happens over the network, and it is the slowest of all the locality levels.

Check out the related configs for tuning this behavior below.

LocalityPreferredContainerPlacementStrategy source code: https://lnkd.in/gZwPCWTa


Transform function in pyspark:
This function is used when you read a data from a file you want to change data type of the column or change the small letter to upper case etc....
Df is the dataframe you read you want to make changes with in this dataframe then using transform function we can achieve it.

General scenario using with column we can change it and applying logic on that column here a new dataframe is getting created it exist old and new column both. 

from pyspark.sql.functions import upper
def to_upper_str_columns(df):
    return df.withColumn("CourseName",upper(df.CourseName))

def apply_discount(df):
    return df.withColumn("discounted_fee",  \
             df.new_fee - (df.new_fee * df.discount) / 100)

def reduce_price(df,reduceBy):
    return df.withColumn("new_fee",df.fee - reduceBy)

# PySpark transform() Usage
df2 = df.transform(to_upper_str_columns) \
        .transform(reduce_price,1000) \
        .transform(apply_discount)

df2 = df.transform(to_upper_str_columns) \
        .transform(reduce_price,1000) \
        .transform(apply_discount)



Multiple columns rename:
df=df.withColumn('city', df.address.city).withColumn('state', df.address.state).withColumn('zipcode', df.address.zipcode)



Unittesting Pyspark pipeline:
https://medium.com/towards-data-science/how-to-test-pyspark-etl-data-pipeline-1c5a6ab6a04b




Spark optimization techniques:
1) Caching 
2) Partitioning
3) Broadcasting
4) Shuffle optimization
5) Data serialization and deserialization
6) Predicate pushdown
7) Code generation
8) Memory management
9) Resource allocation
10) Tuning parameters
11) Vectorization
12) Data compression
13) Off-heap storage
14) Dynamic partition pruning
15) Columnar storage
16) Code profiling
17) Adaptive query execution
18) Off-heap execution
19) Early exit
20) GPU acceleration
21) Broadcast variables
22) Pipelining
23) Delta Lake
24) Auto tuning
25) Query optimization
26) Memory tuning
27) Sampling
28) Tuning the execution environment
29) Dynamic allocation
30) Task scheduling
31) Execution plan caching
32) Window functions
33) Data partition pruning
34) File format optimization
35) Query caching
36) Skewed data handling
37) Data filtering and projection
38) Shuffle tuning
39) Join optimization
40) Broadcast join optimization




Need to clear:
4) Shuffle optimization
6) Predicate pushdown
7) Code generation
10) Tuning parameters
19) Early exit
20) GPU acceleration
26) Memory tuning






Difference Between Parquet & Delta Table ?

Parquet File Format : Parquet is a columnar storage format for large-scale data processing. it is designed to be highly efficient and optimized for bigdata technologies like Apache Hadoop and Apache Spark. Some of the key features of parquet include:

Features of parquet:
-> Columnar Storage
-> Schema Evolution
-> Compression
-> Predicate Pushdown
-> Encoding
-> Platform Independent
-> Interoperability

Delta Table : Delta table is a feature of Apache Delta Lake, an open-source storage layer that sits on top of the data lakes and providers ACID transactions, data versioning, and schema enforcement. Delta tables are stored in Parquet format, but they also include a transaction log that keeps track of all the changes made to the table, allowing for efficient updates and deletes.

Features of Delta Table:
-> ACID Transactions
-> Data Versioning
-> Schema Enforcement
-> Efficient Updates and Deletes
-> Stream Processing
-> Interoperability
-> Time Travel
-> Auditing



1. Explain Spark job repeatedly fails with solution in Spark.?

Issue: Spark job repeatedly fails

Cause: When the cluster is fully scaled and the cluster is not able to manage the job size, the Spark job may fail repeatedly.

Resolution: Run the Sparklens tool to analyze the job execution and optimize the configuration accordingly.


2. Explain FileAlreadyExistsException in Spark jobs with solution in Spark.?

Issue: FileAlreadyExistsException in Spark jobs

Cause: The FileAlreadyExistsException error occurs in the following scenarios:
o  Failure of the previous task might leave some files that trigger the FileAlreadyExistsException errors
o  When the executor runs out of memory, the individual tasks of that executor are scheduled on another executor. As a result, the FileAlreadyExistsException error occurs.
o  When any Spark executor fails, Spark retries to start the task, which might result into FileAlreadyExistsException error after the maximum number of retries.

Resolution:
1.    Identify the original executor failure reason that causes the FileAlreadyExistsException error.
2.    Verify size of the nodes in the clusters.
3.    Upgrade them to the next tier to increase the Spark executor’s memory overhead.




*pyspark left anti join can be achieved by using substract or minus query




Modified after and modifierbefore:

This two options available only in the databricks.

If we want to read file before the it got modified or after modified, all files are available in file location.
Then marking one file timestamp and read files.

df = spark.read.option("header", True).csv("path", modifiedBefore = '2024-01-01T00:00:00')
df = spark.read.option("header", True).csv("path", modifiedAfter = '2024-01-01T00:00:00')



handle corrupt records in pyspark:

This two options available only in the databricks.
For corrupted data a new field will be added to the result set.

df = spark.read.option("header", True).csv("path", columnnameofcorruptrecord = 'errorrows')


# Code:
max_val.first()[0]  -- single value to a variable from a dataframe column
df = spark.range(1, 10)
df.column.isNull()
df.column.isNotNull()
timestamp_diff('MINUTE', timestamp_field1, timestamp_field2)
MINUTE, YEAR, QUARTER, MONTH, WEEK, DAY, HOUR, SECOND.
extract(F.lit('year', field))
year, month, week, d, m, s
date_format(date_field, 'EEEE') --> return day is monday, tuesday...
EEE  Mon, Tues, Wed....
col("date_field") + expr("INTERVAL 1 DAY")
expr("min_count * 1.0/total_count")
to_date("string_field", "yyyyMMdd")
split(content, " ")
explode(array_field)
groupBy("field").agg(F.concat_ws(",", F.collect_list("id")))    
data
3 1 
3 1

return as 
3   1, 3


rowsBetween(Window.unboundedPreceding, Window.currentRow)
rowsBetween(0, 2)    
rowsBetween(-2, 0)


# Json:
## single json
{"customer_id":101, "name":"Raj", "order":["order_id":1]}

## double or more json
[{"customer_id":101, "name":"Raj", "order":["order_id":1]}, {"customer_id":102, "name":"Rajesh", "order":["order_id":2]}]
Both style .option(multiline", "True") should use during reading

## individual json
{"customer_id":102, "name":"Raj", "order":["order_id":1]}
{"customer_id":103, "name":"Raj", "order":["order_id":2]}
multiline not required.

If json has array or map that specific one need to explode it and then access by json style.
struct type can't be explode.

Json is a text-based data format used to trasmit the data over the networks.
dictionary is active, in-memory data structure. reading and modifying data inside code.


Exmaple: dictionary is like an idea in head, json is same idea written in paper to hand over to someone else.




## What happens when you call collect() on a large DataFrame? What should you do instead?
df.collect()
Spark brings all rows from all worker nodes to the driver node.

If the DataFrame is large, this can cause:

Driver out-of-memory
Cluster crash
Slow performance
Network bottleneck
Job failure

What to do instead
Use distributed actions:
df.write.format("delta").save("/mnt/output")

For preview:
df.show(10)




## Explain broadcast joins. When does Spark choose one automatically and when do you force it?
A broadcast join means Spark sends the small DataFrame to every executor, so the big DataFrame does not need shuffle.

When to force broadcast
When you know one table is small but Spark does not choose broadcast because:
Stats are missing
Table size estimate is wrong
Small table is filtered at runtime
Small Table Exceeds Broadcast Threshold  (50MB > 10MB)
Broadcast Disabled
Adaptive Query Execution (AQE) Disabled:
Original table = 100 MB
After filter = 2 MB

Spark still won't broadcast because it made the decision earlier.
With AQE enabled, Spark can change the join strategy during execution.



# try_cast:
try_cast is available in newer versions of Spark SQL (Spark 4.x). It attempts to cast a value and returns NULL instead of throwing an error if the conversion fails.

Ex:
df = df.withColumn(
    "Age_Int",
    expr("try_cast(Age AS INT)")
)

Output:
Age	Age_Int
25	25
30	30
ABC	NULL
45	45


:try_to_date
try_to_date("JD", "yyyy-MM-dd") 
otherthan this format date value, remaining value return as NULL.