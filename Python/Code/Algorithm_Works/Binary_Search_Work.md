1. How binary search works
data = [10, 9, 1, 5,  6,  13, 4, 20]

sort the data first.
binary search will move left or right based on mid point.
mid = (low + high)//2
low = 0 
high = len(data)-1 ==> 7


[1, 4, 5, 6, 9, 10, 13, 20]

6 is the mid point, now key is the target value to check in the data were it exists.

let say if key is 13 then need to move right.
if key is 4 need to move left side
both need to handled in single binary sort.

compare low with high values in while loop and find the target value exist in the data or not.

