nums = [0,0,1,1,1,2,2,3,3,4]
cnt = 1
for i in range(1, len(nums)):
    if nums[i] == nums[i-1]:
        pass
    else:
        nums[cnt] = nums[i]
        cnt = cnt + 1

print(cnt)
print(nums)



