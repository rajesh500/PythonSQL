data1 = [2,4,5,6,1,2,6,8,9]
data2 = [2,4,5,61,2,5]

print(list(set(data1) - set(data2)))


# only first list difference data will get it, if we need to get from both need to iterate one more loop.
for i in set(data2):
    if i not in data1:
        print(i)



ans = list(filter(lambda x: x not in data2, data1))
print(ans)