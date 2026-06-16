from sqlalchemy import create_engine, text
engine = create_engine('postgresql://u61gjpmvjt5prl:p6a67b3b89c0babe7005c17bd8e2af98551fcbdde9aae7f26fd80d45ad0d73024@ec2-34-206-124-133.compute-1.amazonaws.com:5433/db5g29u2cel02j')
connection = engine.connect()
my_query = text("CREATE TABLE batchuat.CBMS_case_number_for_referrals_without_county_name(Application_Process_Queue varchar, Application_Process_Queue_ID varchar, Application_Number varchar,  CBMS_Case_Number varchar,  County varchar,  Name varchar,  Status varchar,  Incorrect_Information_Needed varchar,  Application_Source varchar,  Application_Received_Date varchar,  Application_Processed_Date varchar,  Application_Process_Queue varchar,  Reason_for_Referral_Rejection varchar,  Reason_for_Application_Rejection varchar,  Rejection_Reason_Notes	varchar)")
result = connection.execute(my_query)

