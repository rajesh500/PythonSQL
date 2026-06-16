nums = [1, 3, 2, 6, -1, 4, 1, 8, 2]
k = 5
# average 
# newlist = []


# for i in range(k, len(nums)+1):
#     windowSum = sum(nums[(i-k):i])/k
#     newlist.append(windowSum)

# print(newlist)


# Sum 
# nums = [1, 3, 2, 6, -1, 4, 1, 8, 2]
# k = 5
def max_subarray_sum(nums, k):
    windowSum = 0
    large = 0
    for i in range(k, len(nums)+1):
        windowSum = sum(nums[(i-k):i])
        if windowSum > large:
            large = windowSum
    return large

a = max_subarray_sum(nums, k)
print(a)

