# with open('Data\Data.txt', mode ='r') as file:
#     data = file.readlines()
#     for row in data:
#         print(row.strip())


# # read line by line using readline()
# with open('Data\Data.txt', mode ='r') as file:
#     for i in range(3):
#         print(file.readline().strip())


# # read first and last line using readline()
# with open('Data\Data.txt', mode ='r') as file:
#     firstline = file.readline()
#     for i in file:
#         pass
#     print(firstline)
#     print(i)



# with open('Data\Data.txt', mode ='r') as file:
#     #firstline = file.readline()
#     for i in file:
#         print(i)
#     #print(firstline)


#read n lines from a file using readlines():
# with open('Data\Data.txt', mode ='r') as file:
#     #first_n_lines = file.readlines()[:2] # first n lines
#     last_n_lines = file.readlines()[2:] # first n lines
#     #print(first_n_lines)
#     print(last_n_lines)


# read the file data in reverse order
with open('Data\Data.txt', mode ='r') as file:
    data = file.readlines()
    for row in reversed(data):
        print(row)