data = [2,4,5,6,1,2,6,8,9]

target = 2
# for i in range(len(data)):
#     print(data[i], i)
#     if data[i] == target:
#         del data[i]

# print(data)
new_list = []
for i in data:
    if i != target:
        new_list.append(i)
print(new_list)


new_com = [ i for i in data if i != target ]
print(new_com)