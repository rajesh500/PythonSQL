def nextGreaterElement(nums):
    stack = []
    n = len(nums)
    result = [-1] * n
    for i in range(n):
        while stack and nums[stack[-1]] > nums[i]:
            idx = stack.pop()
            result[idx] = nums[i]
        stack.append(i)
    return result

nums = [2,1,3,2,4,3]
res = nextGreaterElement(nums)
print(res)