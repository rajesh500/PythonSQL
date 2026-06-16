nums = [1, 0, 2, 3, 0, 4, 5, 0]
r = 0

for l in range(len(nums)):
    print(l, 'l')
    if nums[l] != 0:
        nums[l], nums[r] = nums[r], nums[l]
        print(nums, 'nums')
        r = r + 1
        print(r, 'r')
print(nums)
    

nums = [1, 0, 2, 3, 0, 4, 5, 0]
r = 0
l = 0

while r < len(nums):
    if nums[r] != 0:
        nums[l], nums[r] = nums[r], nums[l]
        l += 1
    r += 1
print(nums)
    