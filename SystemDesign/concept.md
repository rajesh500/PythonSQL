10 steps to follow in DE system design interview:
1. Function and non-functional requirement
2. source and target clarifications
3. high level architecture design
4. Design the data model (how it will be queried)
5. Design ingestion
6. Design storage and transformations and compute
7. Orchestration and workflow
8. Fault Tolerance and recovery
9. Monitoring and logging
10. Optimization and Trade-offs

 Inventory data sources and contracts
    identify the major components required to build the system
    Data Ingestion: Kafka, kinesis, apache pulsar, pub/sub
    Data Storage: HDFS, S3, ADLS, snowflake, redshift
    ETL/ELT: spark, flink  (real streaming processing SLA is seconds (fraud detection))
    Data transformation: SQL, pyspark
    Data warehouse: Bigquery, Redshift, snowflake
    Data Serving layer: Elasticsearch, cassandra
    Real-time analytics: Druid, clickhouse  (real time data warehouse)
    Data visualization: PowerBI, tableau

3. high level architecture design
4. Database schema design
5. Data ingestion and processing
6. Data storage and partition
7. Scaling and optimization
8. Fault Tolerance and recovery
9. Monitoring and logging
10. Optimization and Trade-offs.



# 1. Function and non-functional requirement gathering.
Gathering Functional Requirements (The "What")
Focus on specific tasks, data sources, and transformations. 

## 1. Identify Users & Use Cases: 
Who is using the data, and for what purpose (e.g., reporting, machine learning)? \
Identify Users (Actors): Data Analysts (needing reporting tables), Data Scientists (needing raw feature sets), BI Systems (needing API access), and Data Stewards (needing audit logs).

## 1. Data Ingestion Sources: 
Identify APIs, databases, streaming services (e.g., Kafka), or batch logs.

## 1. Transformations & Data Flow: 
Map out the ELT/ETL steps, data validation rules, and schema requirements.
Key Transformation & Data Flow Tasks in Functional Requirements:
Define Data Flow (Source-to-Sink): Map data from source systems to the target data warehouse or data lake, defining ingestion frequencies (batch vs. real-time) and latency requirements.

## 1. Implement Data Transformation Stages:
Bronze (Raw): Ingest raw data in its native format to maintain a full history.
Silver (Cleansed): Filter, de-duplicate, validate, and standardize data types, column names, and formats (e.g., date formats, currency standardization).
Gold (Curated): Aggregate and model data (joins, pivots) to produce analytics-ready datasets, such as star schemas for BI tools.

Define Transformation Logic: Clearly define business rules, such as joining customer CRM data with transactional data, calculating metrics (SUM, AVG), and masking personally identifiable information (PII).

Quality Control Checkpoints: Integrate validation checks at each stage to ensure data completeness and accuracy, using automated tests for transformations.

Data Modeling: Structure data for optimization, such as partitioning in Spark or using columnar formats like Parquet to improve query performance

## 1. Access Patterns: 
How will users consume data? (e.g., SQL queries, API calls, dashboarding)


# non-functional
## Scalability: 
Ability to handle increasing data volume (e.g., TBs to PBs) without performance degradation.
## Reliability/Availability: 
Ensuring pipelines maintain high uptime (e.g., 99.9%) to meet SLA constraints, as discussed on LinkedIn.
## Data Quality/Integrity: 
Maintaining accuracy, consistency, and completeness (e.g., zero data loss).
## Latency/Performance: 
Determining if data needs to be available in real-time (milliseconds) or batch (hours).
## Security & Compliance: 
Implementing encryption at rest/transit and adhering to regulations like GDPR or HIPAA, note Pipeline To Insights.
## Maintainability: 
Ensuring code is modular, well-documented, and easy to update.


# Consistency:
Consistency means that every time someone accesses the system, they get the most recent data. Example: Updates on Share Market or the cart items in E-commerce apps.
# Availability:
Availability means that the system is always up and running even if some part of it are having problems.

# Scalability:
Scalability is all about the size, that is, it refers to the ability of a system to handle the increasing load or traffic in a adequate manner.

# Performance:
Performance is all about how well a system responds to client interactions and executes tasks within desirable time frames. Performance is all about the speed, "how fast the system can complete a task?"

# Vertical Scaling:
Vertical Scaling involves adding more resources to an existing server (like CPU, RAM) to handle increased load. It's simpler but can be limited by hardware constraints and also increases a single point of failure.

# Horizontal Scaling:
Horizontal Scaling involves adding more servers to distribute the load which enhances the scalability across multiple machines.

# Batch Processing:
Batch Processing is a method of processing data where tasks are collected and executed all at once, rather than in real-time. it involves collecting data over a period, processing the data in batches, and then storing the output. Example: Credit cards for daily billing

# Stream Processing:
Stream Processing is a method where continuous streams of data are processed in real-time as they are received. These are designed to handle high-throughput data with low latency.

# Tradeoff between Batch Processing and Stream Processing:

Batch Processing:
Advantages:
Optimizes resource utilization by processing data in bulk.
Suitable for tasks that can tolerate delays in processing.
Tradeoff:
Delays results until all data is gathered and processed.
Not suitable for real-time applications needing immediate data insights or actions.
Stream Processing:
Advantages:
Processes data as it arrives, enabling real-time analysis and immediate action.
Ideal for time-sensitive applications requiring continuous monitoring and quick response.
Tradeoff:
Requires immediate resource allocation and potentially higher operational costs.
May not efficiently handle tasks that can be batched or processed offline.

# Low Latency, High Throughput:
Low Latency, High Throughput: Prioritizes quick response times for individual requests, achieved through efficient resource use. However, this focus may limit simultaneous request handling, potentially reducing overall throughput.

# High Throughput, Higher Latency:
High Throughput, Higher Latency: Maximizes workload processing within a timeframe, often via batch or parallel processing. This strategy can handle many requests concurrently but may result in slightly longer response times due to queueing or resource competition during peak loads.

# Latency:
Latency measures the time it takes for a system to respond to a request or perform an operation.

# Throughput:
Throughput measures the rate at which a system can process or handle a workload within a given time period. It refers to the average volume of data that can be processed in a specific duration.



Questions to Expect (Be Ready)
Scalability:
What if data volume increases 10x?
How does this handle peak load?
Failure Scenarios:
What happens if the source API goes down?
How do you recover from a failed pipeline?

Security:
How do you handle PII/sensitive data?
What about access control?
Operations:
How do you deploy changes?
How do you monitor this?
Who’s on-call when it breaks?

Trade-offs:
Why did you choose X over Y?
What are the downsides of your approach?




Architectures:

Lambda Architecture:
                    spark               presto
            | ---> batch layer   --->| serving | --->| output layer |
Input Layer |                        | layer   |     |              | tableau/Qlikview...
            | ---> speed layer   --->|________ | --->| output layer |
                    spark streaming
                    kafka 
                    flink


Basically combining batch data and real time data in the lambda architecture.
* earlier we have separate architecture for batch processing and real time.

Customer table --> batch daily once
customer --> real data a speed layer

Here combining both data but if the liver data for customer (fraud transaction) doesn't have any chagnes then batch doesn't have the users data then fraud detection won't happen right away may be a day layer.

user case:
Recommendation enginess
fraud detection systems 
OIT Systems 
Realtime log analytics

* serving  layer merge results of both batch and speed layer s to provide unified view for users. It merge pre-computer batch views and realtime updates

limitation:
duplicate code
maintaince hard
Data Quality ()
Two different distrubuted systems to manage 
    one for batch --> system built on  spark    
    another one for speed --> system built on flink


Kappa architecture:
                                                                --> real time consumer
source --> real time data processing layer --> serving layer  |
                                                                --> Batch consumer

Limitations:
Need lot of joins
Reprocess data
need Datawarehouse
very high cost
Late records  

Data lake architecuture:
                       ------- Data storage & processing ----
source --> Ingest --> raw/landing --> transform/processed data --> BI/Reporting/ML/DW/...






CAP Theorem:
Consistency, Availability, Partition tolerance:
Consistency: 
Ex: if there are multiple node, if you connected to any node all of the users has to see same data at the same time no matter 
which node they connect to.

Availability:
ability of a system to respond to requests from users at all times.

Partition tolerance:
ability of a system to continue operating even if there is a network issue.

network partition: any network failures
https://www.geeksforgeeks.org/system-design/cap-theorem-in-system-design/







CDC pipeline:
1. functionan requirement?
    1. user/auditions --> files/tables/report/api/ml/da/...
       data purpose what is the user want to see 

    2. source?  (kafka/streaming)
       volume    
    3. constraints (do/don't)
   
   non functional 

2. source and target clarifications

3. high level architecture

read/write operation is not costly, if we have transformation then only compute cost.
why raw layer?        tracking, downstream fail then source data remains untouched, auditing, debugging, 
                      if business rules changes then reprocess from source.
why silver?           data cleansing(data type fixes, handling missing values, validating schemas), join different sources, deduplication.... business rules.
gold? Aggregated, project-specific and business-ready data.
why can't do directly in gold   
why medallion architecture?
compute cost for silver?
silver to gold cost?
storage cost?

silver/gold doesn't need to be table it can be s3 as well.

4. technologies used in the above architecture diagram
Technologies:

 Inventory data sources and contracts
    identify the major components required to build the system
    Data Ingestion: Kafka, kinesis, apache pulsar, pub/sub
    Data Storage: HDFS, S3, ADLS, snowflake, redshift
    ETL/ELT: spark, flink  (real streaming processing SLA is seconds (fraud detection))
    Data transformation: SQL, pyspark
    Data warehouse: Bigquery, Redshift, snowflake
    Data Serving layer: Elasticsearch, cassandra
    NoSQL:  Cassandra (wide-column), MongoDB (document), Redis (key-value/caching).
    Real-time analytics: Druid, clickhouse  (real time data warehouse)
    Data visualization: PowerBI, tableau
    Monitoring:  Grafana, prometheus.
    Governance:  Collibra, Alation.
    Orichestration:  Airflow.
    Cache: Redis


5. data modeling.

## Data Compliance:
 what data you have, 
 who can touch it, 
 how it is protected, 
 how activity is recorded, and 
 when the data is deleted


 Personally Identifiable Information (PII) 
 protected health information (PHI)
 HIPAA (Health Insurance Portability and Accountability Act of 1996)
 The General Data Protection Regulation (GDPR)
 PCI data (Payment Card Industry Data) 

PII / GDPR
PHI / HIPAA
PCI data / PCI DSS


## Batch processing:
Daily or hourly reporting
Financial reconciliation
Historical analytics
ETL/ELT pipelines
Large-scale transformations where immediate output is not needed


## Limitation:
Results are delayed until the next run
Users may act on stale data
Cannot react instantly to events




## Data Masking:
Original value in the table will not change, during the query time they will see the masking data.
If they viewing the masking in the table that is a static masking.

Dynamic masking:
static masking:

## Dynamic masking:
Base table remain as is (has the original value)
during the query time masking will happen based on the role.

Anonymizer: is a postgresql feature to implement dynamic masking. (install anon)
alter database demodb SET session_preload_libraries = ‘anon’;
CREATE EXTENSION IF NOT EXISTS anon CASCADE;
SELECT anon.init();

SELECT anon.start_dynamic_masking();
SECURITY LABEL FOR anon
ON COLUMN employees.email
IS 'MASKED WITH FUNCTION anon.fake_email()';

original value replace with fake value.

CREATE ROLE data_analyst LOGIN PASSWORD 'secure_password';

SECURITY LABEL FOR anon
ON ROLE data_analyst
IS 'MASKED';

GRANT SELECT ON employees TO data_analyst;
Login as data_analyst.
select * from employees
id |     name      |            email             |  salary
----+---------------+------------------------------+----------
  1 | Alice Smith   | fake.email.1@example.com     | 82345.00

anonymizer:
https://postgresql-anonymizer.readthedocs.io/en/latest/masking_functions/

anon.random_date(), anon.random_string(n),  anon.random_zip(), anon.random_phone(p)
anon.random_hash(seed),  anon.random_gps_coordinates(), anon.random_point_in_box(Box)

anon.fake_email(), anon.fake_city(), anon.fake_zipcode(), address, city, company, country....

Note: If you don't want to touch the main table create a view and accessing data from it.
Same approach for dynamic masking.

Static masking.
create a view on the base table and in the view define the rule based access.
If the user is login then he able to see the data as masked, other wise in the view still it has the original values only.

create or replace view customer_vw select as 
select 
CASE WHEN pg_has_role(current_user, 'pii_full_access', 'MEMBER') THEN ssn ELSE '***-**-' || right(ssn, 4)
END AS ssn
from customer.

create a role revoke all access on schema and grant usage access the role.
now he is able to view the mask data only.


## Encryption in Postgresql:
pgcrypto  extension, which allows for column-level encryption.
pgp_sym_encrypt() --> encrypt data during the insert
pgp_sym_decrypt() --> decrypt during the query time.