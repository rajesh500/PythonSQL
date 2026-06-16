ar1 = [1, 5, 10, 20, 40, 80]
ar2 = [6, 7, 20, 80, 100]
ar3 = [3, 4, 15, 20, 30, 70, 80, 120]

d={}
new_arr = ar1 + ar2 + ar3
print(new_arr)

# AP-1
ind = 0

for i in new_arr:
    if i in d:
        val = d[i]
        d[i]= val+1
    else:
        d[i]=1

com_element = []
for key, value in d.items():
    if value ==3:
        com_element.append(key)

print(com_element)



# AP-2
from collections import Counter, OrderedDict
c = Counter(new_arr)
print(c.most_common(2))


