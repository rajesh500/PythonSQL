
with open('Data\Data.txt', 'r') as data:
#     first_line = data.readline()
#     last_line = None
#     for file in data:
#         if file is not None:
#             last_line = file

# print(first_line, 'first_line')
# print(last_line, 'last_line')


# count number of lines
    count = 0
    for file in data:
        count = count + 1
        
print(count)