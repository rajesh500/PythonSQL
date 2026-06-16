Types of Data Models:
1. Conceptual
2. Logical
3. Physical

Conceptual: 
* High-level view 
* Entities and thier relationship

Logical:
* Includes attributes and relationship
* No concern for data types and DBMS

Physical:
* Real Implementation
* Data Types, indexes, constraints, partitions.

OLTP 
Normalization

OLAP  (combination of both normalization and denormalization)
Dimensional Data Model


Cloud DWH modeling:
snowflake, databricks, synapse analytics, big query, redshift.


ETL layers:   old on-premise architecture.
stage layer   --> cleansing 
transform layer --> modifing or transforming the data
serving layer --> end layer


stage layer types:
1. persistent layer:
appending the data

2. Transient layer:
replace old data with new data every run.


raw layer(stage) --> Enriched --> Curated.
Curated layer doing the data model.


Medallion Architecture:
Bronze --> Silver --> Gold
Raw(Bronze) 
Enriched(Silver) 
Curated(Gold)   

Silver layer do upsert operations.



Relational Databases (SQL) (e.g., MySQL, PostgreSQL, Oracle):
Uses: Structured data requiring strong consistency, such as financial transactions, ERP, and CRM systems. Data is organized into tables with rows and columns.
NoSQL Databases (Non-relational) (e.g., MongoDB, DynamoDB):
Uses: Unstructured or semi-structured data, high-volume data, and flexible schemas. Ideal for social media feeds, real-time web applications, and big data.
Graph Databases (e.g., Neo4j):
Uses: Analyzing complex relationships and interconnected data, such as social networks, fraud detection, and recommendation engines.
Time-Series Databases (e.g., InfluxDB):
Uses: Monitoring IoT sensors, tracking application metrics, and analyzing financial data where time is the primary axis.
Columnar / Wide-Column Databases (e.g., Cassandra, HBase):
Uses: Analytical queries, logging, and large-scale data warehousing (Big Data).
In-Memory Databases (e.g., Redis):
Uses: Extreme low-latency processing, caching, and real-time analytics by storing data in RAM.
Object-Oriented Databases:
Uses: Handling complex data structures in engineering, CAD, and simulation applications.
Vector Databases (e.g., Pinecone):
Uses: Storing data as vector embeddings for AI, machine learning, and semantic searches. 




Fact table vs. dimension table (transaction data example)
Using point-of-sale transaction data, the cleanest mental model is: facts = what happened (events + numbers), dimensions = the descriptive “who/what/where/when/how” you use to analyze those events.
1) Fact table (transaction events)
Fact_SalesLine (most common design)

Grain: one row per transaction line item (each product on a receipt)
Columns

Foreign keys (join to dimensions): DateKey, StoreKey, CustomerKey, ProductKey, PaymentMethodKey, PromotionKey (optional)
Degenerate dimensions (identifiers kept in the fact): ReceiptNumber, TransactionId (often no separate dimension table)
Measures (aggregations): Quantity, UnitPrice, GrossAmount, DiscountAmount, NetAmount, TaxAmount, CostAmount



Example fact rows (simplified):


TransactionId      Line        DateKey     StoreKey        CustomerKey     ProductKey      Qty     NetAmount
T1001               1           20260201       12               501         3009            2       19.98
T1001               2           20260201        12              501         1440            1       5.99
T1002               1           20260201        12              777         3009            1       9.99



2) Dimension tables (descriptive context)
Each dimension has a surrogate key (e.g., ProductKey) and lots of attributes for filtering/grouping.

Dim_Product:
ProductKey, SKU, ProductName, Brand, Category, Subcategory, Size

Dim_Customer:
CustomerKey, CustomerId, Segment, LoyaltyTier, SignupDate

Dim_Store:
StoreKey, StoreId, StoreName, Region, City

Dim_Date:
DateKey, CalendarDate, DayOfWeek, Month, Quarter, Year, FiscalPeriod

Example dimension rows (simplified):

Dim_Product:
ProductKey  SKU     ProductName       Category      Brand
3009        A-123   Trail Mix 12oz      Snacks      Acme
1440        B-555   Sparkling Water     Beverages   AquaCo



Dim_Store:
StoreKey    StoreId   StoreName           Region
12          1012      Denver - Union        West



3) How they work together (star schema)
You analyze facts by joining on keys:

“Net sales by month and category in the West region”

Sum Fact_SalesLine.NetAmount
Group/filter using Dim_Date.Month, Dim_Product.Category, Dim_Store.Region



Quick differentiators:
Fact table: many rows; numeric measures; keys to dimensions; represents events at a defined grain.
Dimension table: fewer rows; descriptive attributes; used for slicing/dicing; often “slowly changing.”



SCD (slowly changing dimensions):
SCD type-0 -- once's record created no change
SCD type-1 -- keep only latest record
SCD type-2 -- keep historical data (old and new)
SCD type-3 -- keep historical data ( limited history only current and previous, very previous not maintain)
SCD type-4 -- Has two dimensions table, one has latest and other has history.
SCD type-6 -- 


SCD type3:
first value is Irving, second is Coppell and third is Farmers branch
In Scd type3 table only prev_field as coppell and current has farmers branch, Irving will not exist.

Dimension table design for customer:
Fields required:
Customer_ID -- primary key
customer_sk is surogate key 
effective_start_date
effective_end_date
is_current_flag
created_date
lastmodifieddate
optinal: etl_batch_id, source_system

these are mandatory field for creating any scd type-2 dimension table
SCD type-2 surogate key is mandatory because
If customer has two entire, customer_id will be same we can't say these are unique records.
using surogate key only, will be defined as unique records.

SCD type-1 and SCD type-3 surogate key is optinal
SCD tpye can be implemented only in dimension table
Normalization can be implemented only in dimension table

effective_start_date and effective_end_date is required specific scenario of scd type-2
If a customer effective from jan1 - june30 current flag is N
july1 - Dec31 current flag is Y. (future entry in June1)
if we need to get a customer address for the time frame of june1-june30.
if we didn't maintain  effective_start_date and effective_end_date based only current flag we will incorrect address.
If we maintain these fields based on start_date end end_date, can be pulled correct address.

If a table has created_date and current_flag why two.
If try to pull based on created date need to partition and assign a row number/max pulled the latest one.If the data size is hugh
then it will cause performance issues. if we used current_flag field then instead of write complex query just based on flag we can pull it.



Dimensions:
dimensions are descriptive tables that provide the business context for the numeric data stored in fact tables(measures like revenue, units and cost).

Types of dimensions:
Conformed Dimensions:
Thier is no specific structure of this dimension table.
If a dimension is used multiple fact tables and it is called conformed dimension.
Example: Customer data is used in sales, marketing, orders etc...)

Junk Dimension:
Junk fields will be store in a table and  define this key in the fact table.
Junk fields like multiple fields combinations
example:
Junk_key_ID     Gender      Marital Status
    1           Male        Single
    2           Male        Married
    3           Male        Div
    4           Female      Single
    5           Female      Married
    6           Female      Div

Fact table data:
product:

TaxID   DateKey     AccountKey  MerchantKey     Amount  Currency JunkID
90001   20250115    20010       701              24.50   USD       2
90002   20250115    20010       888              180.00  USD       4
90003   20250116    20011       555              60.00   USD       6

Example2:
JunkID  packed  Shipped   Delivered   
1          Y       N        N
2          Y       Y        N
3          Y       Y        Y 


Role-playing Dimension:
A role-playing dimension is a single dimension table that is reused in a model under multiple “roles” by joining it to a fact table through different foreign keys.

Example:
Datekey      Date        Day     Month       Quater        Year
20250115    2025-01-15  Wed       Jan           Q1         2025
20250116    2025-01-16  Thur      Jan           Q2         2025
20250118    2025-01-18  Fri       Jan           Q3         2025

Fact table:
TxnID       TxnDateKey      PostDateKey     SettleDateKey       Amount
9001        20250115        20250116        20250118            24.50
9002        20250116        20250116        20250116            180.00

Static Dimension:
A static dimension is a dimension table whose attributes are effectively constant for analytics—changes are rare, and you typically overwrite in place.

Outtriggered Dimension: Dimension table links to another dimension table.

Inferred Dimension:
An inferred dimension is a placeholder dimension record created when a fact arrives before the full dimension data is available (common in late-arriving master data). It lets you load the fact with a valid surrogate key now, then “fill in” the dimension attributes later.

Example:
customer order without sign will have only customer first and last names.
Once he order based on his order detail dimension table data will be updated.

Nike order without signup ...
save the memberdata and update the dimension table with amount, place, etc...


Degenerated Dimension:

Example: invoice number, ord number, receipt nbr....



** fact table 99.99% is insert and update, it is very light operation for update....

fact tables:
Types of fact tables:
1. Transaction: transaction data one row per event(etc.. orders, calls, sales..)
2. periodic: On the above table taking a snapshot on daily/weekly/monthly/quaterly/yearly store in this table, these kind is periodic. (daily inventory...)
3. accumating: one row per instance (when a customer order a items then first entry will be on this table then 
when order is ready new record appended, order shipped, order delivered...)
4. factless fact: non-measuric values (example customer promo-day)


Normalization:
Before introducing normal form data is store in a specific way is 
ID      Name        address
1       John        address1, address2, address3


When normal forms introduced
1NF:each comma separate value should be a record.
ID      Name        address
1       John        address1
1       John        address2
1       John        address3

2NF: 1NF + remove partial dependencies, where non-prime attribute depend only part of composite key.
Example:
table:
ID      Course      Name        Grade
1       C251        Ann           A

Here ID and course are composite, where grade field is dependend on course.
because a person took a course and what grade he got for that course. which means grade field is depend up on course.
Here course is not completely depend on composite key. Hence this data need to be in separate table.


Ex:  2NF data should be look like this
Table1:
ID           Name        
1            Ann         

Table2:
ID            Course            Grade
1              C251                A


3NF:   2 NF + Non-key columns should not depend on other non-key columns

Below example data is 
Why it violates 3NF

DeptName and DeptLocation do not depend directly on EmployeeID.
They depend on DeptID (a non-key attribute in this table).
That’s a transitive dependency:
EmployeeID → DeptID → DeptName, DeptLocation

EmployeeID   EmployeeName   DeptID   DeptName    DeptLocation
10           Ana Rivera       3      Finance     Dallas
11           Sam Nouri        3      Finance     Dallas
12           Li Wang          5      IT          Chicago


3NF form data:
EmployeeID      EmployeeName        DeptID
10              Ana Rivera          3
11              Sam Nouri           3
12              Li Wang             5


Departments (PK = DeptID)
DeptID      DeptName        DeptLocation
3           Finance         Dallas
5           IT              Chicago


Data Modeling:
Two types of data modeling 
1. Transactional data model
2. Dimensional data model

Transactional data model:
A transactional (OLTP) model is designed to run the business (capture day-to-day events accurately).
Data:
Many normalized tables (3NF), lots of foreign keys, minimal redundancy.

Dimensional data model:
dimensional (OLAP) model is designed to analyze the business (query and aggregate quickly for reporting).
data: snowflake, star schema


Below model is for transactional not for OLAP.
Design of Pizza store:
Entities:
Orders  --> fact
Order_Items --> fact 
Customers --> Dimension
Customer_Address --> Dimension
Product --> Dimension 
Payment --> facts

Customer:
Customer_SK, Customer_id, name, phone, created_Date, updated_dt, current_flag, start_date, end_date

Address:
Address_sk, customer_id, address1, address2, city, state, zipcode, updated_dt, current_flag, start_date, end_date

Product:
product_sk, prod_id, product_name, price, active, created_Date, updated_dt, current_flag, start_date, end_date

Orders:
Order_id, store_id, customer_id, order_type, status, created_date

OrderItems:
Order_item_id, order_id, product_id, quantity, price, notes, created_date

payment:
payment_id, order_id, method, amount, authorized_at, status, created_date

Delivery:
order_id, address_id, driver_employee_id nullable, dispatched_at, delivered_at, delivery_status.

can be design more and more tables.
example:
discount, tax/fee,...


If we need to design same for the OLAP.
order and orderitem need to be in one table, data is going to be in denormalized form.


Data Modeling tools free:
Draw.io
Lucidchart
DBdiagram.io


Three levels of Data Modeling:
1. Conceptual: High-level overview of data and its relationships - focuses on business concepts.
Points: No technical knowledge etc...
only focus on business need and requirements.
Example: time, product, sales, store tables..
No attributes

2. Logical: Detailed model defining data elements and their relationships - indepedent of technology.
Ex: Attributes and relationships on the tables(PK, FK)
Points: No concern with physical storage or database performance

3. Physical: Implementation - ready model specifying how data is stored in the database system.
Includes table structures, column data types, indexes and constraints
Database
Addresses performance, security and storage


Relationships:
Cardinality
one-to-many  (one record in a table can link to many records in another table)
many to one
many to many

Dimension → Fact = one-to-many (1:N): one dimension record (e.g., one Customer) can be referenced by many fact rows (many Sales).
Fact → Dimension = many-to-one (N:1): each fact row points to one record in each related dimension (via foreign keys


Data Modeling optimization techniques:
Denormalization
indexing
partitioning 
caching
dimensional modeling (star vs snowflake)
query optimization
other


How do you ensure data quality and integrity in your data models?
I ensure data quality and integrity by implementing primary and foreign key constraints, unique indexes and validation rules. I also collaborate with stakeholders to define data requirements, use automated data validation tools and regularly audit data for 
discrepancies. This approach helps maintian reliable and consistent data across the system.


Types of data modeling:
1. Conceptual / Logical / Physical modeling
2. ER (Entity - Relationship)
2. Normalized (3NF) modeling
3. Dimensional modeling (Star/Snowflake)
4. Data Vault (Raw Vault + Business Vault + Marts)
5. Medallion / Layered lakehouse (Bronze–Silver–Gold)
6. One Big Table (OBT) / Wide table
7. Event-driven / Clickstream modeling
8. Graph modeling
9. NoSQL data modeling
10. Object-Oriented Modeling 
11. Hierarchical & network modeling



Types of Databases:
Relational: data is in tableaur format(structured)

NoSQL: desgined for semi-structured, un-structured and structured can also be handled. NoSQL databases support horizontal scalability which means increasing the capacity by adding more servers (or nodes) rather than upgrading the resources of a single server, known as vertical scaling.
In nosql db divided into multiple. 

Document: data is in JSON, BSON or XML format.
Ex: MongoDB, DynamoDB, cosmosDB
key Document
101 {"order":{"order_id":"98765", "items":[{"item_name":"keyboard","quan":"1"}]}}

Key-Value: data is in key and value pair 
Ex:   Redis, RocksDB, HAZELCAST, DynamoDB
key     value
k1      AA, BB, CC

Graph: data is graph format (node  and edge)
Neo4J, CosmosDB 
Columnar Databases: same as realtional only the difference data store is    different. here data store in column wise (DB's snowflake, bigquery, redshift).

Time-series:  designed for handling time-stamped or time-series data. events like 
aggregation are very high time-series is used.
monitoring, network, sensor, trading....
Druid

Object-Oriented 
 




Before Data Governance:
Without governance, businesses may deal with duplicate records, missing information, and incorrect reports. This leads to bad insights and poor decisions.

** inconsistancy of data, duplicate, bad data, reliablility, trust on data, security, compliance, accuracy etc....

Data Governance:
Data governance is the process of managing, organizing and protecting data by defining rules, policies, and controls to ensure accuracy,  security and compliance.

A well-implemented data governance strategy establishes who can access data, how it is stored, and how changes are tracked.

Example Banking...
Access Control:
Only authorized employees can view or modify sensitive customer details.

Data Quality Checks:
Systems detect and prevent duplicate accounts or incorrect transactions.

Audit Trails:	
Every data change is logged, allowing errors to be traced and corrected.

Regulatory Compliance:
The bank follows legal frameworks like GDPR to protect customer information.

Maintains Data Accuracy and Consistency:
Without this duplicate records, missing information, and incorrect reports.
with data governance:
A strong governance framework ensures that data is always consistent, updated, and properly formatted across systems.


Enhances Data Security and Privacy:
Unauthorized access to sensitive data can result in cyberattacks, financial losses, and reputational damage.
Data Governance enforces strict access controls, allowing only authorized users to handle confidential information. It also ensures that sensitive data is encrypted, protected, and properly classified to prevent leaks.
Example: hospital patient records.

Helps in Compliance with Regulations:
Companies must follow data protection laws like GDPR, HIPAA, and CCPA to avoid heavy fines. Governance ensures that data is collected, stored, and used according to legal standards. It also keeps records of who accessed data, when, and for what purpose, making compliance audits easier.


Improves Business Decisions and Analytics:
incorrect data decisions wrong
correct data better decisions.

Reduces Operational Costs and Risks:
Fixing poor-quality data is expensive. Businesses spend time and resources correcting errors, which slows down processes and increases costs. Governance prevents these issues by implementing data validation, standardization, and automated quality checks.


Benefits of Data Governance:
Clear Understanding of Data
Improved Data Quality
Better Data Integration with a Data Map
Ensures Regulatory Compliance



GDPR:
General Data protection regulation (GDPR):
1. Lawfulness, fairness, and transparency
   * Data must be processed legally.
   * User must know:
        * what data is collected
        * why its collected

--> No hidden data usage

2. Purpose Limitation:
    * Collect data only for a specific purpose
    * Don't reuse it for something unrelated

--> Email for login cannot be used for marketing without consent.

3. Data Minimization:
    * Collect only necessary data
--> Don't ask for phone number if not needed.

4. Accuracy:
    * Data must be
        * correct
        * up-to-date
5. Storage Limitation
    * keep data only as long as needed.
--> Delete or anonymize when no longer needed.

6. Integrity and Confidentiality(Security):
    * Protect data from:
        * breaches
        * unauthorized access

--> Use:
    * encryption
    * access control

7 Accountability:
    * Organization must:
        * demonstrate compliance
        * maintain records
        * implement policies
--> you must prove for follow GDPR


HIPPA:
1. Privacy Rule:
protect PHI
only use/share data when necessary
pateints have rights:
    access their data
    request corrections

2. Security Rule:
protect electronic PHI

3. Breach Notification Rule


PHI and PII has the same priciples like GDPR.


Difference Between Star and Snowflake Schema
Feature               Star Schema                                                    Snowflake Schema

Structure       Central fact table connected to dimension tables        Fact table connected to normalized dimension tables            
Data Normalization      Denormalized dimension tables                   Normalized dimension tables
Performance             Faster query execution due to fewer joins       Slower query performance due to multiple joins
Design Complexity       Simple and easy to understand                   Complex design with multiple levels of relationships
Space Usage             Uses more storage due to denormalization        Uses less storage due to normalization
Data Redundancy         Higher data redundancy                          Lower data redundancy
Foreign Keys            Fewer foreign keys                              More foreign keys
Use Cases               Best for large datasets and quick ad-hoc queries  Best for structured, predictable queries
Query Complexity        Low query complexity                             High query complexity due to multiple joins
Maintainability         Easier to maintain due to simple design          More difficult to maintain due to complexity
Scalability             Scalable but may encounter performance issues with large data volumes           More scalable for very large data sets due to normalization
Suitability for BI Tools    Ideal for BI tools and quick reporting       Better for systems that require detailed reporting and data analysis
Data Integrity          Lower data integrity due to redundancy          Higher data integrity due to normalization
Updates and Modifications   More difficult to update due to denormalization     Easier to update as data is normalized
Learning Curve          Easier to learn and implement                   More complex to learn and implement