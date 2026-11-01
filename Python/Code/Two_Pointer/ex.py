# def hasTripletSum(arr, target):
#     n = len(arr)
#     arr.sort()
#     res = []
#     # Fix the first element as arr[i]
#     for i in range(n - 2):
        
#         # Initialize left and right pointers with 
#         # start and end of remaining subarray
#         l = i + 1
#         r = n - 1
        
#         requiredSum = target - arr[i]
#         while l < r:
#             if arr[l] + arr[r] == requiredSum:
#                 res.append([arr[i], arr[l], arr[r]])
#             if arr[l] + arr[r] < requiredSum:
#                 l += 1
#             else:
#                 r -= 1
#     return res

# if __name__ == "__main__":
#     arr = [1, 4, 45, 6, 10, 8]
#     target = 13
#     r = hasTripletSum(arr, target)
#     print(r)


def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    nums.sort()
    res = []
    n = len(nums)
    for i in range(n-2):
        start = nums[i]
        left = i + 1
        right = i+2
        while right < n:
            l = nums[left]
            r = nums[right]
            if start + l + r == 0:
                res.append([start, l , r])
            right = right + 1
    return res

r = threeSum([-1,0,1,2,-1,-4])
print(r)