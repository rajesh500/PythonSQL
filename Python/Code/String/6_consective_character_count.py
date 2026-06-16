test_str = "geekksforgggeeks"

count = 1
empt_list  = []
empt_dict = {}

for i in range(len(test_str)-1):
    if test_str[i] == test_str[i+1]:
        count = count + 1
    else:
        empt_list.append(count)
        #empt_dict[test_str[i]] = count
        count = 1
empt_list.append(count)
#empt_dict[test_str[i]] = count

print(empt_list)
#print(empt_dict)


#Approach-2:
from itertools import groupby
res = [ len(list(j)) for i , j in groupby(test_str)]
print(res)