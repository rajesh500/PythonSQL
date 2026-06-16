x = -121
st = str(x)
rev_str = ''
for i in range(len(st)-1, -1, -1):
    rev_str = rev_str+st[i]

print(type(rev_str))


abc = 'abcdef'
print(''.join(reversed(abc)))