import bisect

arr = [1, 3, 4, 5, 5, 5, 67, 123, 125]
x = 5
left = bisect.bisect_left(arr, x)
right = bisect.bisect_right(arr, x)

print('left', left)
print('right', right)

all_indices = list(range(left, right))
print(f"Indices where x={x} is found: {all_indices}")