s = "GeeksforGeeks"
d = 2

left_rotate = s[:d]
str1 = s[d:]
print(left_rotate)
print("left roration", str1+left_rotate)

right_rotation = s[-d:]
str2 = s[:-d]
print(right_rotation +str2)



s = "GeeksforGeeks"
d = 3

print(s[-3:])

l = len(s)-d
print(s[:l])
