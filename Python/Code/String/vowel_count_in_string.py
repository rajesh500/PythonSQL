#Apporach1
str = 'GeeksforGeeks'

count_list = [str.count('a'), str.count('e'), str.count('i'), str.count('o'), str.count('u')]
count = 0
for i in count_list:
    count = count +int(i)

print(count)

#Apporach2
d= {}

for i in str:
    if i in d:
        d[i] +=1
    else:
        d[i]=1
dcount = 0
for i in 'aeiou':
    if i in d:
        dcount = dcount + int(d[i])
print('dcount', dcount)