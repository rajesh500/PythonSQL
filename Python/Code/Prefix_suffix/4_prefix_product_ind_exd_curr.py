# include current element
# arr = [1, 2, 3, 4]
# n = len(arr)
# prefix = [0] * n
# prefix[0] = arr[0]

# for i in range(1, n):
#     prefix[i] = prefix[i-1] * arr[i]
# print(prefix)


# exclude current element
arr = [1, 2, 3, 4]
n = len(arr)
prefix = [0] * n
prefix[0] = arr[0]

for i in range(1, n):
    prefix[i] = prefix[i-1] * arr[i-1]
print(prefix)
