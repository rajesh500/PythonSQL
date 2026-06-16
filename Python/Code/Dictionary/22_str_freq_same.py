#s = "xxxxyyzz"
s = 'xyyz'
s1 = list(set(s))
#print(s1)

from collections import Counter
count = Counter(s)
val = list(count.values())
print(max(val), min(val))
if (max(val) - min(val)) == 1:
    print('Yes')
else:
    print('No')

dchar = ''
for i in s1:
    if max(val) == count.get(i):
        print(i, 'has the highest value and possible to delete a char')
        dchar = dchar + i


emp_list  = []
for i in s:
    if i in emp_list:
        pass
    else:
        emp_list.append(i)

print(''.join(emp_list))
    