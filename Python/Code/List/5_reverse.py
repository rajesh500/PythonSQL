data = [2,4,5,6,1,2,6,8,9]

data.reverse()
print(data, 'reverse')
print(list(reversed(data)), 'reversed')

rev =  [2,4,5,6,1,2,6,8,9]
#print(rev[::-1])


for i in range(len(rev)-1,-1, -1):
    print(rev[i])


print(sorted(data, reverse=True))  # descending order reverse list
print(sorted(data, reverse=False))  # ascending order reverse list.


a ='python'
n= len(a)-1
i = 0
emt_str = ''
while n >= 0:
    emt_str += a[n]
    print(n)
    n = n-1
print(emt_str)
