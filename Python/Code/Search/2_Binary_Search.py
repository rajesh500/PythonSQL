data = [10, 9, 1, 5,  6,  13, 4, 20]
data.sort()
print(data)
low = 0
high = len(data)-1
key = 13
found = False

# 7 // 2 divides 7 by 2, which gives 3.5.
# The // operator rounds down to the nearest integer, so the result is 3.
while low<= high and  found == False:
    mid = (low + high)//2
    print(mid, 'mid number')
    print(data[mid], 'middle value')
    if key == data[mid]:
        found = True
    elif key < data[mid]:    # left move
        high = mid - 1
        print('left side')
    else:                   # Right move
        low = mid + 1
        print('right side')
if found:
    print("Key Found", data[mid])
else:
    print("key not Found")