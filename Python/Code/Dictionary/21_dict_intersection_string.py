s1 = 'BOBthebuilder'
s2 = 'fBoOkBIHnfndBthesibuishlider'

# chk = ''
# for i in s1:
#     if i in s2:
#         chk = chk+i 
    
# if chk == s1:
#     print("possible")

# else:
#     print("Not Possible")


# Ap-2
from collections import Counter 

count1 = Counter(s1)
count2 = Counter(s2)

#print(count1)
possible = True
for i in count1:
    if count1[i] > count2[i]:
        possible = False
        break

if possible:
    print("possible")
else:
    print("not possible")