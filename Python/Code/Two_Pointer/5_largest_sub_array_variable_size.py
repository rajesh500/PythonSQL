# small sub array and long sub array both code almost same only few 
# instead of infinity define 0 and if windowSum == target: and finding highest value condition.
# note: code will return the sub array start and end position this need to catch and pull the data.

from typing import Optional
def min_sub_array(target, data):
    left = 0 
    sub_arr_len = 0
    window_sum = 0
    pos = 0
    for right, i in enumerate(data):
        window_sum = window_sum + i 
        print(window_sum)

        while  window_sum >= target:
            if window_sum == target:
                curr_sub_arr = len(data[left:right+1])
                if curr_sub_arr > sub_arr_len: 
                    sub_arr_len = curr_sub_arr
                    pos = (left, right)        

            window_sum = window_sum - data[left]
            left = left +1
    return pos
   
data = [2, 1, 5, 1, 3, 2]
#0, 2, 1, 5, 2, 3, 2,4,6]
target = 7 
res = min_sub_array(target, data)
print(res)
i, j = res
print(i, j)
print(data[i:j+1])

