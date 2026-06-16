nums = [1,3,5,6]
target = 7

if target in nums:
    print(nums.index(target))
else:
    for i in range(len(nums)):
        print(i)
        if  nums[i] > target:
            print(i)
        #print(len(nums))
        if int(len(nums))-1 == int(i):
            print('Hi')
            print(len(nums))