# sub array sum
# data = [2,1,5,1,3,2]
# k = 3
# n= k
# sublist = []
# sublist_total = 0
# for i in range(len(data)):
#     len_check = data[i:k]
#     if len(len_check) == n:
#         sublist_total = sum(len_check)
#         sublist.append(sublist_total)
#         k = k+1
#     else:
#         break

# print(sublist)        
# print(max(sublist))

# problem with this approach unnessary sublist, k value increase, break statement, length check

# large sub array value
# data = [2,1,5,1,3,2]
# k = 3
# def maxsubarray_sum(data, k):
#     n= k
#     large = 0
#     for i in range(len(data)):
#         len_check = data[i:k]
#         if len(len_check) == n:
#             sublist_total = sum(len_check)
#             k = k+1
#             if sublist_total > large:
#                 large = sublist_total
#     return large

# print(maxsubarray_sum(data, k))




### this approach is good,increasing and decreasing the left and right with sum
'''  description '''
'''  first summing the elements with key value then iteration starts from k value.
     Increase and decrease one value and add both to the sum first we calculated.
     In this approach no need to think of break loop or last iteration.
'''

# this approach is efficient 
# data = [2,1,5,1,3,2]
# k = 3

# def subarray_sum(data, k):
#     if len(data) < k:
#         return -1
    
#     windowSum = sum(data[:k])
#     maxSum = windowSum

#     for i in range(k, len(data)):
#         windowSum = windowSum + data[i] - data[i-k]
#         maxSum = max(windowSum, maxSum)
#     return maxSum


# a = subarray_sum(data, k)
# print(a)





# instead of using max, with in the code itself finding the large value


# data =  [1, 3, 2, 6, -1, 4, 1, 8, 2]
# #[2,1,5,1,3,2]
# k = 5

# def subarray_sum(data, k):
#     if len(data) < k:
#         return -1
    
#     windowSum = sum(data[:k])
#     large = 0

#     for i in range(k, len(data)):
#         windowSum = windowSum + data[i] - data[i-k]
#         if windowSum > large:
#             large = windowSum

#     return large


# a = subarray_sum(data, k)
# print(a)



# another apporach of left and right
# do n't calculating total  directly,  slicing and suming it.

# Sum 
nums = [1, 3, 2, 6, -1, 4, 1, 8, 2]
k = 5
def max_subarray_sum(nums, k):
    windowSum = 0
    large = 0
    for i in range(k, len(nums)+1):
        print(nums[(i-k):i])
        windowSum = sum(nums[(i-k):i])
        if windowSum > large:
            large = windowSum
    return large

a = max_subarray_sum(nums, k)
print(a)
