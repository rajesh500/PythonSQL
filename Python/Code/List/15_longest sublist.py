nested_list = [[1, 2, 3], [4, 5], [6, 7, 8, 9], [1,2]]

a = 1
for i in nested_list:
    if len(i) > a:
        a = len(i)
        sublist = i

print(sublist)



print(max(nested_list, key=len))

a, b = 10, 5
print(max(a, b))

xyz = [1,24,3,6,4,8,9]
print(max(xyz))