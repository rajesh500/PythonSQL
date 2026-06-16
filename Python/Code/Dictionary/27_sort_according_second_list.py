a1 = [4, 1, 3, 3, 2] 
a2 = [3, 1]

ord_list = []
for i in a2:
    for j in a1:
        if i == j:
            ord_list.append(j)

# print(ord_list)
nonord_list = sorted(list(set(a1)- set(a2)))

newList = ord_list + nonord_list
print(newList)