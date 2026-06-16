# include current element
# arr = [2, 1, 5, 3, 4]
# n = len(arr)
# suffix = [0] * n
# print(suffix)
# suffix[-1] = arr[-1]
# print(suffix)

# for i in range(n-2, -1, -1):
#     suffix[i] = max(suffix[i+1], arr[i])
# print(suffix)



# arr = [2, 1, 5, 3, 4]
# n = len(arr)
# last = n-1
# suffix = [0] * n
# suffix[last] = arr[last]

# for i in range(n-2, -1, -1):
#     suffix[i] = max(suffix[i+1], arr[i])
# print(suffix)


# exclude current element
arr = [2, 1, 5, 3, 4]
n = len(arr)
suffix = [0] * n
print(suffix)
suffix[-1] = float("-inf")
print(suffix)

for i in range(n-2, -1, -1):
    suffix[i] = max(suffix[i+1], arr[i+1])
print(suffix)