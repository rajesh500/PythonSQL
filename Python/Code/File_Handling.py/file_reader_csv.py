# import csv

# with open('Data\employeedata.csv', mode = 'r', newline='', encoding='utf-8') as data:
#     csv_reader = csv.reader(data, delimiter=',')
#     #header = next(csv_reader)
#     for row in csv_reader:
#         print(row)


# read data in key value pair format
import csv

# with open(r'Data\employeedata.csv', mode = 'r', newline='', encoding='utf-8') as data:
#     csv_reader = csv.DictReader(data)
#     #header = next(csv_reader)
#     for row in csv_reader:
#         print(row['Name'])

# write data in key value pair format
data_list = [{'Name':'Rock', 'Age':'53', 'Height':'55'}]
fieldnm = ['Name', 'Age', 'Height']

with open(r'Data\employeedata.csv', mode = 'a', newline='') as wdata:
    writer = csv.DictWriter(wdata, fieldnames=fieldnm)
    #writer.writeheader()
    writer.writerows(data_list)