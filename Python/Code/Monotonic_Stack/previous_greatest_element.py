def nextGreaterElement(nums):
    stack = []
    n = len(nums)
    result = [-1] * n
    for i in range(n):
        while stack and nums[stack[-1]] <= nums[i]:
            stack.pop()
        if stack:
            result[i] = nums[stack[-1]]
        stack.append(i)
    return result

#nums = [15, 10, 18, 12, 4, 6, 2, 8]
nums = [4, 5, 2, 10, 8]
res = nextGreaterElement(nums)
print(res)