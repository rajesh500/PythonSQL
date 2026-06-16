nums = [-2,1,-3,4,-1,2,1,-5,4]

total = nums[0]
max_value = nums[0]
temp_index = 0
curr_value = 0
i = 1
for right, i in enumerate(nums):
    if total < 0:
        total = 0
        temp_index = right
        print('temp_index', temp_index)
    total = total + i
    max_value =  max(max_value, total)
    if max_value > curr_value:
        curr_value = max_value
        left = temp_index
        end = right
print(nums[left:end+1])
print(max_value)



# nums = [-2,1,-3,4,-1,2,1,-5,4]

# total = nums[0]
# max_value = nums[0]
# for i in range(1, len(nums)):
#     if total < 0:
#         total = 0
#     total = total + nums[i]
#     max_value =  max(max_value, total)
# print(max_value)