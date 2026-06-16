# Prefix SUM:
# problem can be solved using slicing but if the data size is hugh then we will face performance issue
# here even though using a loop but operation happening but two elements which will give hugh performance.

arr = [2, 1, 5, 3, 4]
n = len(arr)
# include current element and find the max.

# prefix = [0] * n
# print(prefix)
# prefix[0] = arr[0]
# print(prefix)

# for i in range(1, n):
#     prefix[i] = min(prefix[i-1], arr[i])
# print(prefix)


# exclude current element and find the max
# from previous element we will find the max

prefix = [0] * n
prefix[0] = float("inf")
print(prefix)

for i in range(1, n):
    prefix[i] = min(prefix[i-1], arr[i-1])
print(prefix)




