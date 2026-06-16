# positive and negative circular slicing

#s = [10,8,7,7,5,3,9,6]
#k = 4
s = [2,4,9,3]
k = -2
n = len(s)
empt_list = []
count = 1
suffix = ''
suff = ''
cnt = 1
if k == 0:
    print([0]*n)

elif k >= 1:
    for i in range(n):
        prefix = s[i+1:][:k]
        if len(prefix) < k:
            suffix = s[:count]
            count = count + 1
        empt_list.append(sum(prefix)+ sum(suffix))
#print(empt_list)
else:
    for i in range(n):
        m = i+n+k
        pref = s[m:]
        if len(pref) < (k*(-1)):
            suff = s[:cnt][k:]
            cnt = cnt + 1
        empt_list.append((sum(pref)+sum(suff)))
print(empt_list)