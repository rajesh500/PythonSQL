import csv
#import pyspark

insert = 'INSERT INTO prod_backup.t_auth_encmbr_enrollment_20230104_ats (cnt_hour_care, idn_auth, dte_care) VALUES '
with open(r"C:\Users\rjakkula\Documents\enrollment_data.csv") as f:
    for row in csv.reader(f):
        insert_statement = (insert + str(row) + ";").replace('[', '(').replace(']', ')')
        print(insert_statement)
