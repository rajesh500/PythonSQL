
nums = [1,2,3,4,6,9]
#[1,2,9,4,6,3]       # data need to be in sorted order.
target=10

def two_sum_sorted(target, nums):
    left = 0
    right = len(nums)-1
    newlist = []
    while left < right:
        sum = nums[left] + nums[right]
        if sum == target:
            #newlist.append([left, right])  # all match
            return (left, right)     # first match 
        if sum < target:
            left = left + 1
        else:
            right = right - 1
    return newlist

res = two_sum_sorted(target, nums)
print(res)



# # is_palindrome

# def is_palindrome(data):
#     left = 0 
#     right = len(data)-1

#     while left < right:
#         if data[left] != data[right]:
#             return False
#         left = left + 1
#         right = right - 1
#     return True

# data = "racecar"
# res = is_palindrome(data)
# print(res)




# # Read/write compaction (same direction, “keep” in-place)

def keep_in_place(data, val):
    write = 0
    for read in range(len(data)):
        if data[read]  != val:
            data[write] = data[read]
            write += 1
            
    return write




data = [0,1,0,3,12]    
val = 0 
res = keep_in_place(data, val)
print(data[:res])