# max value from the subarray
def max_val_subarray(data, k):
    sublist = []
    for i in range(k, len(data)+1):
        left = i-k
        right = i
        sublist.append(max(list(data[left:right]))) 
    return sublist



data = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
res = max_val_subarray(data, k)
print(res)

# out:
# [3, 3, 5, 5, 6, 7]