s = 'abbey'
s1 = s.lower()

fchar = s[:1]
prev_char = 1

possible = ''
for i in s1:
    if prev_char <= ord(i):
        prev_char = ord(i)
        possible = 'YES'
    else:
        possible = 'NO'

if possible == 'YES':
    print('YES')
else:
    print('NO')

