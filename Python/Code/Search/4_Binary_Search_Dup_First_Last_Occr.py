# Finding first occurance either side
data = [1, 2, 2, 2, 3, 3, 4, 4, 5]
# first = None
# low = 0
# high = len(data)-1
# key = 3

# while low <=  high:
#     mid = (low+high)//2
#     if data[mid] == key:
#         first = mid
#         high = mid - 1
#     elif data[mid] < key:
#             low = mid + 1
    
#     else:
#         high = mid-1

# print(f'index of {key} is at', first)

# # Explanation of iteration execution:
# iteration-1: 
# low = 0, high = 8, first = none, key = 2
# while 0<=8: True
# mid = 0+8//2 ==> 4
# if data[4]==key: 3==2: False
# elif data[4] < key: 3<2: False
# else:
#     h= 4-1 = 3

# iteration-2:
# while 0<= 3: True
# mid = 0+3//2 ==> 1
# if 2 == 2: True 
#     first = 1
#     high = mid - 1 ==> 1-1=0

# iteration-3:
# while 0<=0: True
#     mid = 0
#     if 2==1: False
#     elif: 1<2:True 
#         low = mid + 1 ==> 0+ 1 = 1

# iteration-4:
# while 1<= 0: false exit

# ----- if key = 4
# low = 0, high = 8
# while 0<= 8: True
# mid = 4
# if 4 ==3: False
# elif 3 < 4:
#     low = 4+ 1 = 5
#     high = 8

# Iter-2:
# while 5 <= 8:
#     mid = 6
#     if 4 == 4:
#         first = 6:
#         high = 6-1 = 5
#         low = 5
# Iter-3:
# while 5 <= 5:
#     mid = 5
#     if 4 ==3: False
#     elif 3 < 4: True
#         low = 5+1 = 6
#         high = 5

# iter-4:
#     while 6<= 5: False exit  from loop.



# Last occurance.
last = None
low = 0
high = len(data)- 1
key = 4

while low <= high:
    mid = (low + high)//2
    if key == data[mid]:
        last = mid
        low = mid + 1
    elif key < data[mid]:
        high = mid - 1  
    else:
        low = mid + 1

print(f'index of {key} is at', last) 


# # explanation:
# It-1:
# while 0<= 8: Truemid = 4
# if 2 ++4: False
# elif key < data[mid]:
#     high = mid - 1 ==> 4 -1 = 3
#     low = 0
    
# It-2:
#     while 0<=3:
#         mid = 3/2 ==1
#         if 2==2: True 
#         last = mid = 2
#         low = mid + 1 = 2
#         low = 2, high = 3


# It-3:
#     while 2 <= 3:
#     mid = 2
# if 2==2:
#     last = 2
#     low = 3, high = 3

# It-4:
#     while 3<= 3:
#     mid = 3
# if 2==2:
#     last = 3
#     low = 3+1 = 4:
#     high = 3

# It-5:
#  4<=3: False exit loop


# # Right side move:
# while 0<8: True 
# mid = 4
# if 4==3:
# elif 4<3:
# else: low= mid+1 
# low = 5
# high = 8

# It-2:
# while 5<=8:
#     mid = 6 
#     if 4==4:
#         last = 6
#         low = 7
#         high = 8

# It-3:
# while 7<=8:
#     mid = 7 
#     if 4==4:
#         last = 7
#         low = 7+1 = 8
#         high = 8
    
#     It-4:
#     while 8<= 8:
#         mid = 8
#         if 4 ==5: False
#         elif 4 < 5: True 
#         high = 8-1 = 7

#     It-5:
#     while 8<= 7: False exit loop

