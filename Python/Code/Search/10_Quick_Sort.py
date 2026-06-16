# # pivot is first element, ascending order  [17, 26, 31, 44, 56, 93]
# # condition data[left] <= pivot and data[right] >= pivot.
# # pivot element swap with right with first

# # pivot is first element, descending order [93, 56, 31, 44, 26, 17]
# # conditon data[left] >= pivot and data[right] <= pivot.
# # pivot element swap with right with first


def pivot_find(data, first, last):
    pivot = data[first]
    left = first+1
    right = last

    while True:
        while left <= right and data[left] <= pivot:
            left = left + 1                                     # increase one position
        while left <= right and data[right] >= pivot:
            right = right - 1                                   # increase one position
        
        if right < left:                                        # cross
            break
        # elif left <= right:
        #     data[first], data[right] = data[right], data[first]
        else:
            data[left], data[right] = data[right], data[left]   # swap left with right when condition fail (data[left] <= pivot, data[right] >= pivot)
        print(data, '1')
    data[first], data[right] = data[right], data[first]
    print(data, '2')
    return right                                                # pivot position return


def quick_sort(data, first, last):                              # sub list function.
    if first < last:                                            
        p = pivot_find(data, first, last)
        quick_sort(data, first, p-1)                            # sub list left side
        quick_sort(data, p+1, last)                             # sub list right side

# main
data = [56,26,93,17,77, 31]
n= len(data)
quick_sort(data, 0, n-1)
print(data)










# pivot is last element, ascending order  [17, 26, 31, 44, 56, 93]
# condition data[left] <= pivot and data[right] >= pivot.
# pivot element swap with left with last

# pivot is last element, descending order [93, 56, 31, 44, 26, 17]
# conditon data[left] >= pivot and data[right] <= pivot.
# pivot element swap with left with last

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
        find_pivot(data, first, a-1)
        find_pivot(data, a+1, last)

data = [56,26,93,17,31,44]
first  = 0
last = len(data)-1
quick_sort(data, first, last)
print(data)