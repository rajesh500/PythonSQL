test_str = 'geeksforgeeks 33 best'
empt_str = ''
for i in test_str:
    if i.isspace():pass
    else:
        empt_str +=i

print(len(empt_str))


print(test_str.split())
a = ''.join(test_str.split())
print(len(a))


print(test_str.replace(" ", ""))

# geeksforgeeks33best