nested_list = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]

sng_list = []
for i in nested_list:
    for j in i:
        sng_list.append(j)

print(sng_list)