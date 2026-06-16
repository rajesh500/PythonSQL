# Move zero to end

arr = [5,8,13,0,1,0,3,12]
slow = 0
for fast in range(len(arr)):
    if arr[fast] != 0:
        arr[slow], arr[fast] = arr[fast], arr[slow]
        print(arr)
        slow = slow+1
        
print(arr)