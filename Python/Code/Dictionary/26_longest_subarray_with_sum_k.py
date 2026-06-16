arr = [10, 5, 2, 7, 1, -10]
k = 15

# slicing
print(arr[0:6])

# lengthy approach 
grow_list = []
for index_start in range(len(arr)):
    for index_end in range(index_start+1, len(arr)+1):
        sublist = arr[index_start:index_end]
        grow_list.append(sublist)

for m in grow_list:
    #print(sum(m))
    if k == sum(m):
        print(m)


# this is brute force not recommended only need to solving using DSA.
# Hashing / Two pointer 






