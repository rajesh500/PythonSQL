s = "geeksforgeeks"
d = {}
for i in s:
    if i in d:
        d[i] +=1
    else:
        d[i]=1

print(''.join(d))
ss= sorted(set(s))   
print(''.join(ss))