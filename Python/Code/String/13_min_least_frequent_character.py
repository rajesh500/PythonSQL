test_str = "GeeksforGeeks"

d={}
for i in test_str:
    if i in d:
        d[i] = d[i]+1
    else:
        d[i]=1
# it will print only one least frequency character or word.        
print(min(d, key=d.get), 'min method')

# it will print only one least frequency character or word.        
print(max(d, key=d.get), 'max method')

for i in d:
    if d[i]<=1:
        print(i, 'is the least frequenct character')

# using list comprehension
res = [i for i in d if d[i]<=1 ]
print(res)