import os 
import psycopg2
import pandas as pd
from sqlalchemy import create_engine, text

# r refers raw string
file_path = 'C:\\Users\\rjakkula\\Documents\\DE\\ReportsPOC\\RE231.xlsx'
cred_path = 'C:\\Users\\rjakkula\\Documents\\DE\\db_credentials.csv'

if os.path.isfile(file_path):
    os.remove(file_path)
else:
    print("Path didn't exist")    


''' reading a local file for db credentials '''
def db_crdntls_engine(re231_report_query):
    pdf = pd.read_csv(cred_path, header=None,  names=['host', 'database', 'user', 'password', 'port', 'environment'], index_col=False)
    envrmnt_vrble = pdf.where(pdf["environment"] == "UAT").dropna()
    pdf_list = envrmnt_vrble.iloc[0,:].to_list()
    hostname = pdf_list[0]
    database = pdf_list[1]
    username = pdf_list[2]
    password = pdf_list[3]
    port = pdf_list[4]

    db_connection = 'postgresql://'+ username + ':' + password + '@' + hostname + ':' + port + '/' + database
    print(db_connection)

    # Read all the data from stage table
    engine = create_engine(db_connection)
    rdf_cw = pd.read_sql_query(re231_report_query, engine)
    rdf_li = pd.read_sql_query(re231_report_query, engine)
    rdf_tf = pd.read_sql_query(re231_report_query, engine)
    report_data = pd.read_sql_query(re231_report_query, engine)
    column_renames(rdf_cw, rdf_li, rdf_tf, report_data)

''' data pull, database queries required for the report '''
def db_queries():
    re231_select = 'select * from batchuat.t_re231_stg where pgm_type = '
    re231_fltr_cw = 'CW'
    re231_fltr_li = 'LI'
    re231_fltr_tf = 'TF'
    re231_order_by = ' order by child_age'
    re231_query_cw = re231_select + "'" + re231_fltr_cw + "'" + re231_order_by
    re231_query_li = re231_select + "'" + re231_fltr_li + "'" + re231_order_by
    re231_query_tf = re231_select + "'" + re231_fltr_tf + "'" + re231_order_by
    #print(re231_query_cw)

    # Querying backend table with required field and data.
    report_query = ''' select 
    (select name from salesforceuat.t_county__c where cde_county__c::varchar = county__c::varchar) County,
    start_date__c, 
    end_date__c  
    from salesforceuat.canned_report_request__c 
    where id = (select max(id) from salesforceuat.canned_report_request__c where report_id__c = 'RE231') '''

    db_crdntls_engine(re231_query_cw)
    db_crdntls_engine(re231_query_li)
    db_crdntls_engine(re231_query_tf)
    db_crdntls_engine(report_query)
    

''' dataframe column name renaming '''
def column_renames(rdf_cw, rdf_li, rdf_tf, report_data):
    rdf_cw.rename(columns={"report_id": "Report ID", "child_age":"Child Age", "total_no_of_unique_children":"Total No of Unique Children", "avg_expenditure_per_child":"Average Expenditure Per Child", "total_cost_of_care":"Total Cost Of Care", "pgm_type":"Program Type", "createddate":"Created Date"}, inplace=True)
    rdf_li.rename(columns={"report_id": "Report ID", "child_age":"Child Age", "total_no_of_unique_children":"Total No of Unique Children", "avg_expenditure_per_child":"Average Expenditure Per Child", "total_cost_of_care":"Total Cost Of Care", "pgm_type":"Program Type", "createddate":"Created Date"}, inplace=True)
    rdf_tf.rename(columns={"report_id": "Report ID", "child_age":"Child Age", "total_no_of_unique_children":"Total No of Unique Children", "avg_expenditure_per_child":"Average Expenditure Per Child", "total_cost_of_care":"Total Cost Of Care", "pgm_type":"Program Type", "createddate":"Created Date"}, inplace=True)
    detail_tab_func(rdf_cw, rdf_li, rdf_tf, report_data)

#create a Pandas Excel writer using XlsxWriter as the engine
writer = pd.ExcelWriter(file_path, engine='xlsxwriter')

''' Writing data into detail tab and styling the page'''
def detail_tab_func(rdf_cw, rdf_li, rdf_tf, report_data):
    rdf_cw.to_excel(writer, sheet_name='Details', index=False, startrow=7)
    rdf_li.to_excel(writer, sheet_name='Details', index=False, startrow=17)
    rdf_tf.to_excel(writer, sheet_name='Details', index=False, startrow=27)

    wbsb = writer.book
    wbsh = writer.sheets["Details"]
    #Detail tab data
    detail_frmt =  wbsb.add_format({'align':'right', 'bold':True})
    detail_title_frmt =  wbsb.add_format({'bold':True, 'font_size':14})
    detail_tab_report_title =  wbsb.add_format({'bold':True, 'font_size':11})
    wbsh.write('A1', "RE231 - Expenditures by Program Type and Age", detail_title_frmt)
    wbsh.write('A7', "Child Welfare Payments", detail_tab_report_title)
    wbsh.write('A17', "Low Income Payments", detail_tab_report_title)
    wbsh.write('A27', "TANF Payments", detail_tab_report_title)
    wbsh.write('B2', "County:", detail_frmt)
    wbsh.write('B3', "Report Description:", detail_frmt)
    wbsh.write('B4', "Care Begin Date:", detail_frmt)
    wbsh.write('B5', "Care End Date:", detail_frmt)
    #Detail tab formating
    detail_frmt2 =  wbsb.add_format({'align':'left'})
    #Detail tab heading rows A1:A5
    county_name = report_data.county.to_string(index = False)
    startdate = report_data.start_date__c.to_string(index = False)
    enddate = report_data.end_date__c.to_string(index = False)
    wbsh.write('C2', county_name, detail_frmt2)
    wbsh.write('C3', "A report for expenditures by program type and child age for the requested time interval.", detail_frmt2)
    wbsh.write('C4', startdate, detail_frmt2)
    wbsh.write('C5', enddate, detail_frmt2)
    #Detail tab formating
    wbdetail_frmt = wbsb.add_format()
    wbdetail_frmt.set_align('center')
    # Detail tab cell size define
    wbsh.set_column(0, 0, 20, wbdetail_frmt)
    wbsh.set_column(1, 1, 10, wbdetail_frmt)
    wbsh.set_column(2, 2, 28, wbdetail_frmt)
    wbsh.set_column(3, 3, 30, wbdetail_frmt)
    wbsh.set_column(4, 4, 20, wbdetail_frmt)
    wbsh.set_column(5, 5, 20, wbdetail_frmt)
    wbsh.set_column(6, 6, 15, wbdetail_frmt)
    wbsh.set_column(7, 7, 30, wbdetail_frmt)

''' Legends tab and styling the page '''
def legends_tab_func():
    # creating empty dataframe for Legends tab
    Lengeds_df = pd.DataFrame()
    Lengeds_df.to_excel(writer, sheet_name='Legends')
    wbsb_lt = writer.book
    wbsh_lt = writer.sheets["Legends"]
    #formating tab
    wbsh_lt_frmt =  wbsb_lt.add_format({'bold':True})
    wbsh_lt_frmtt = wbsb_lt.add_format({'bold':True, 'fg_color': '#a39f9e'})

    # Legends tab column A
    wbsh_lt.write('A1', "Where the program type changes for a child’s care over the time interval requested, it is expected that the number of unique children will count the child as often as this occurs.  Meaning, if a case was Low Income on the first care date the report was requested and then moved to TANF for any length of time for the care period requested, the child is considered for both the LI and TANF program type data.")
    wbsh_lt.write('A5', "Low Income Payments", wbsh_lt_frmtt)
    wbsh_lt.write('A6', "Child Age", wbsh_lt_frmt)
    wbsh_lt.write('A7', "Child's age on the first care date of time interval requested")
    wbsh_lt.write('A8', "Total")
    wbsh_lt.write('A10', "TANF Payments", wbsh_lt_frmtt)
    wbsh_lt.write('A11', "Child Age", wbsh_lt_frmt)
    wbsh_lt.write('A12', "Child's age on the first care date of time interval requested")
    wbsh_lt.write('A13', "Total")
    wbsh_lt.write('A15', "Child Welfare Payments", wbsh_lt_frmtt)
    wbsh_lt.write('A16', "Child Age", wbsh_lt_frmt)
    wbsh_lt.write('A17', "Child's age on the first care date of time interval requested")
    wbsh_lt.write('A18', "Total")

    # Legends tab column B
    wbsh_lt.write('B5', "", wbsh_lt_frmtt)
    wbsh_lt.write('B6', "Total Number of Unique Children", wbsh_lt_frmt)
    wbsh_lt.write('B7', "Total Number of Unique Children")
    wbsh_lt.write('B8', "Total Number of Unique Children")
    wbsh_lt.write('B10', "", wbsh_lt_frmtt)
    wbsh_lt.write('B11', "Total Number of Unique Children", wbsh_lt_frmt)
    wbsh_lt.write('B12', "Total Number of Unique Children")
    wbsh_lt.write('B13', "Total Number of Unique Children")
    wbsh_lt.write('B15', "", wbsh_lt_frmtt)
    wbsh_lt.write('B16', "Total Number of Unique Children", wbsh_lt_frmt)
    wbsh_lt.write('B17', "Total Number of Unique Children")
    wbsh_lt.write('B18', "Total Number of Unique Children")

    # Legends tab column C
    wbsh_lt.write('C5', "", wbsh_lt_frmtt)
    wbsh_lt.write('C6', "Average Expenditure per Child", wbsh_lt_frmt)
    wbsh_lt.write('C7', "The total payments for requested time interval divided by the total number of unique children by age.")
    wbsh_lt.write('C8', "Average Expenditure per Child")
    wbsh_lt.write('C10', "", wbsh_lt_frmtt)
    wbsh_lt.write('C11', "Average Expenditure per Child", wbsh_lt_frmt)
    wbsh_lt.write('C12', "The total payments for requested time interval divided by the total number of unique children by age.")
    wbsh_lt.write('C13', "Average Expenditure per Child")
    wbsh_lt.write('C15', "", wbsh_lt_frmtt)
    wbsh_lt.write('C16', "Average Expenditure per Child", wbsh_lt_frmt)
    wbsh_lt.write('C17', "The total payments for requested time interval divided by the total number of unique children by age.")
    wbsh_lt.write('C18', "Average Expenditure per Child")
    # setting cell size in the excel
    wbsh_lt.set_column(0,0, 55)
    wbsh_lt.set_column(1,1, 30)
    wbsh_lt.set_column(2,2, 90)

detail_tab_func()
legends_tab_func()
writer.close()



