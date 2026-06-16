str = 'geeksforgeeks_is_best'
a = str.replace('_', ' ').split()
print('a', a)
empt_str = ''
for i in a:
    print(i.capitalize())
    empt_str = empt_str + i.capitalize()

print(empt_str)
