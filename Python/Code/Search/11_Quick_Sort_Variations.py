
# # pivot is first element, ascending order  [17, 26, 31, 44, 56, 93]
# # condition data[left] <= pivot and data[right] >= pivot.
# # pivot element swap with right with first

# # pivot is first element, descending order [93, 56, 31, 44, 26, 17]
# # conditon data[left] >= pivot and data[right] <= pivot.
# # pivot element swap with right with first

def find_pivot(data, first, last):
    pivot = data[first] 
    left = first+1
    right = last

    while True:
        while left <= right and data[left] >= pivot:
            left = left + 1
        while left <= right and data[right] <= pivot:
            right = right - 1
        
        if right < left:
            break
        else:
            data[left], data[right] = data[right], data[left]
    data[first], data[right] = data[right], data[first]
    return right


def quick_sort(data, first, last):
    if first < last:
        a = find_pivot(data, first, last)
        quick_sort(data, first, a-1)
        quick_sort(data, a+1, last)

data = [56,26,93,17,31,44, 3,2,1,100]
first  = 0
last = len(data)-1
quick_sort(data, first, last)
print('pivot first element and ascending/descending order', data)








# # pivot is last element, ascending order  [17, 26, 31, 44, 56, 93]
# # condition data[left] <= pivot and data[right] >= pivot.
# # pivot element swap with left with last

# # pivot is last element, descending order [93, 56, 31, 44, 26, 17]
# # conditon data[left] >= pivot and data[right] <= pivot.
# # pivot element swap with left with last

def find_pivot(data, first, last):
    pivot = data[last] 
    left = first
    right = last-1

    while True:
        while left <= right and data[left] >= pivot:
            left = left + 1
        while left <= right and data[right] <= pivot:
            right = right - 1
        
        if right < left:
            break
        else:
            data[left], data[right] = data[right], data[left]
    data[last], data[left] = data[left], data[last]
    return left




def quick_sort(data, first, last):
    if first < last:
        a = find_pivot(data, first, last)
        quick_sort(data, first, a-1)
        quick_sort(data, a+1, last)

data = [56,26,93,17,31,44, 3,2,1,100]
first  = 0
last = len(data)-1
quick_sort(data, first, last)
print('pivot last element and ascending/descending order', data)





# ## random elements as pivot element.
# # swap the random element has first element and rest of process is same
# # random element is first element


# def find_pivot(data, first, last):
#     import random 
#     rindex = random.randint(first, last)
#     data[first], data[rindex] = data[rindex], data[first]

#     pivot = data[first]
#     left = first + 1
#     right = last 

#     while True:
#         while left <= right and data[left] <= pivot:
#             left = left + 1
#         while left <= right and data[right] >= pivot:
#             right = right - 1
        
#         if right < left:
#             break
#         else:
#             data[left], data[right] = data[right], data[left]
#     data[first], data[right] = data[right], data[first]
#     return right


# def quick_sort(data, first, right):
#     if first < right:
#         p = find_pivot(data, first, last)
#         quick_sort(data, first, p-1)
#         quick_sort(data, p+1, last)

# # Main
# data = [56,26,93,17,31,44, 3,2,1,100]
# first  = 0
# last = len(data)-1
# quick_sort(data, first, last)
# print(data)


# # out [1, 2, 3, 17, 26, 31, 44, 56, 93, 100]