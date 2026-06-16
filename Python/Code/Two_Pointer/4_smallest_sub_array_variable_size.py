
from typing import Optional

def min_sub_array(target, data):

    left = 0 
    len_check = float("inf")
    window_sum = 0
    pos = 0

    for right, i in enumerate(data):
        window_sum = window_sum + i 

        while window_sum >= target:
            curr_len = right - left + 1
            if curr_len < len_check:
                len_check = curr_len
                pos = (left, right)
            window_sum = window_sum - data[left]
            left = left + 1
    return pos


data = [2, 1, 5, 2, 3, 2]
target = 7 
res = min_sub_array(target, data)
i, j = res
print(i, j)
print(data[i:j+1])

# # i, j are the positions, using position need to retrieve the elements.
# # cur_len is sub array length, instead of checking length, this way need to rigth in the two pointers.
# # float("inf") is positive infinity, default taking infinity and first sub array length assigning it to it.
# # Note: data element of last one should less than the target.






# instead of find the subarray length size with right - left + 1
# use slicing concet below and solve it.
from typing import Optional

def min_sub_array(target, data):

    left = 0 
    len_check = float("inf")
    window_sum = 0
    pos = 0

    for right, i in enumerate(data):
        window_sum = window_sum + i 

        while window_sum >= target:
            curr_len = len(data[left:right+1]) 
            if curr_len < len_check:
                len_check = curr_len
                pos = (left, right)
            window_sum = window_sum - data[left]
            left = left + 1
    return pos


data = [0, 2, 1, 5, 2, 3, 2,4,6]
target = 7 
res = min_sub_array(target, data)
i, j = res
print(i, j)
print(data[i:j+1])


