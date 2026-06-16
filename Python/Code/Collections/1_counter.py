from collections import Counter

# string
str1 = 'Hello'
ctr2 = Counter(str1)
print(ctr2)


d = {'A':1, 'B':2, 'C':4, 'C':5, 'D':8}
ctr3 = Counter(d)
print(ctr3)


data = [1,2,4,3,2,1,3,5,6,7,8,9,4,2,13,4,5,23,4,5,6,6]
ctr1 = Counter(data)
print(ctr1)


data = [1,2,4,3,2,1,3,5,6,7,8,9,4,2,13,4,5,23,4,5,6,6]
ctr1 = Counter(data)
print(ctr1[13])   # Count of 13 in list., if not 0 will return.


ctr1.update([20, 10, 11])  # updating 
print(ctr1)

print(list(ctr1.elements()), 'elements')

print(ctr1.most_common(1))


print(ctr1[3])


ctr1.subtract([])

ctr1 = Counter([1, 2, 2, 3])
ctr2 = Counter([2, 3, 3, 4])
print(ctr1 + ctr2)   # Addition
print(ctr1 - ctr2)   # Subtraction 
print(ctr1 & ctr2)   # Intersection
print(ctr1 | ctr2)   # Union