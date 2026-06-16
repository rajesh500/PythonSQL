data = [2,4,5,6,1,2,6,8,9]

first_element = data[0]
print(first_element)

last_element = len(data)
print(data[last_element-1])


print(data[1:-1])  # 1 is start and -1 is end.

data = [2,4,5,6,1,2,6,8,9] 

new_list = []
for i, j in enumerate(data):
    if i == 0 or i == len(data)-1:
        pass
    else:
        new_list.append(j)

print(new_list, 'new_list')