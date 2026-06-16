data = [2,4,5,6,1,2,6,8,9]

print(sorted(data, reverse=True)[1])   # descending order 
print(sorted(data)[-2])                 # sort with negative index


largest= 0
smallest = 0
for i in data:
    if largest < i:
        smallest = largest
        largest=i
print(smallest)


