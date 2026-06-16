data = [2,4,5,6,1,2,6,8,9,20, 21,50, 23,56]

n = 3

rotate_left = data[:n]
rotate_right = data[n:]
new_data = rotate_right+rotate_left
rotate_right.extend(rotate_left)
print(rotate_right)



del data[:n]
data.extend(rotate_left)
print(data)



