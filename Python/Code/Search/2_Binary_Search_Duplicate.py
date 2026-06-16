# # First 
# data = [10, 9, 1, 5,  6,  13, 4, 20, 5, 5, 5, 5]
# data.sort()
# print(data)
# key =  5 

# low = 0
# high = len(data)-1
# found = False

# while low <= high and found == False:
#     mid = (low + high)//2
#     #print('mid value', mid)
#     if key == data[mid]:
#         first = mid 
#         #print('first', first)
#         high = mid - 1
#         #print('high', high)
#     elif key < data[mid]:
#         high = mid - 1
#     else:
#         low = mid + 1
#         found = True

# print('first', first)




# First good option
#data = [10, 9, 1, 3,  6, 6,  13, 4, 20, 5, 5, 5, 5]
#data.sort()
data = [1, 3, 4, 5, 5, 5, 5, 6, 6,  9, 10, 13, 20]
print(data)
key =  5 

low = 0
high = len(data)-1
found = False

while low <= high and found == False:
    mid = (low + high)//2
    #print('mid value', mid)
    if key == data[mid]:
        first = mid 
        #print('first', first)
        high = mid - 1
        #print('high', high)
    elif  data[mid] < key:
        low = mid + 1
        #print('low', low)
        # found = True
    else:
        right = mid - 1

print('first', first)




# # Last 

# #data = [10, 9, 1, 5,  6,  13, 4, 20, 5, 5, 5, 5]
# data = [10, 9, 1, 3,  6,  13, 4, 20, 5, 5, 5, 5]
# data.sort()
# print(data)
# low = 0
# high = len(data)-1
# last = None 
# key = 5


# while low <= high:
#     mid = (low+high)//2
#     if key == data[mid]:
#         last = mid
#         low = mid + 1
#     elif data[mid] > key:
#         high = mid - 1
#     else:
#         low = mid + 1

# print('last', last)
