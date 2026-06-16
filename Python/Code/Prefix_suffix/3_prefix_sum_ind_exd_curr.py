arr = [2, 1, 3, 4]

# include current element
# n = len(arr)
# prefix = [0] * n
# prefix[0] = arr[0]
# print(prefix)

# for i in range(1, n):
#     prefix[i] = prefix[i-1] + arr[i]

# print(prefix)

# exclude current
# when working on excluding current element, consider previous element as 0 or -/+ inf 
n = len(arr)
prefix = [0] * n
prefix[0] = 0
print(prefix)

for i in range(1, n):
    prefix[i] = prefix[i-1] + arr[i-1]
print(prefix)