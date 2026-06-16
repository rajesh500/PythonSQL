s = 'aaabbcaa'
res = ''
n = len(s)
prev = ''
count = 0
for i in range(n):
    cur = s[i]
    if prev:
        if prev != cur:
            res = res + prev + str(count)
            count =  0
    prev = cur
    count = count + 1
    #if i == n-1:
res = res + cur + str(count)
print(res)
