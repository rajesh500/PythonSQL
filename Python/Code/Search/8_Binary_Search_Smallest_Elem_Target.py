### larger than the target but it should be a small elements
#data = [1, 2, 4, 5, 6, 6, 8]

# # largest element
# low = 0
# high = len(data)-1
# key = 5
# large = None

# while low <= high:
#     mid = (low+high)//2
#     if data[mid] > key:
#         large = mid
#         high = mid -1
#     elif  data[mid] < key:
#         low = mid + 1
#     else:
#         low = mid + 1  # because need to find the first largest element than the target.


# print('largest element greater than target at index', large)


        
# # Smallest element
# data = [1, 2, 3, 4, 5, 6, 8]
# low = 0 
# high = len(data)-1
# key = 5
# small = None


# while low<= high:
#     mid = (low+high)//2
#     if data[mid] < key:
#         small = mid
#         low = mid + 1
#     elif data[mid] > key:
#         high = mid - 1
#     else:
#         low = mid + 1
    
# print('smallest element less than target at index', small)




# Both handled in one block:

data = [1, 2,  4, 6, 8]
large = None
small = None
low = 0
high = len(data)-1
key = 5

while low<= high:
    mid = (low+high)//2
    if data[mid] < key:
        small = mid
        low = mid + 1
    
    elif data[mid] > key:
        large = mid
        high = mid - 1 
    
    else:
        print("Found")


print('smallest element less than target at index', small)
print('largest element less than target at index', large)
