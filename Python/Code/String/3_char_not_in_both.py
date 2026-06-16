s1 = "geeksforgeeks"
s2 = "geeksquiz"


no_comm1 = ''
no_comm2 = ''
for i in s1:
    if i not in s2:
        no_comm1 += i
        print(i)


for j in s2:
    if j not in s1:
        no_comm2 += j
        print(j)

print(no_comm1, no_comm2)



print(set(s1) & set(s2))  # intersection
print(set(s1) ^ set(s2))  # difference 
print(set(s1) - set(s2))  # minus from 1
print(set(s1) | set(s2))