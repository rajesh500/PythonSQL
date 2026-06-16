
a = [1, 2, 3, 2, 1]
str_a = [str(i) for i in a]
print(''.join(str_a))

print(a[::-1])

print(list(reversed(a)))
if a==list(reversed(a)):
    print('True')

