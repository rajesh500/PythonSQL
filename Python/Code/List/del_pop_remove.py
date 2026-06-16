#Remove elements by index
a = [1, 2, 3, 2, 3, 4, 5]

# use del
del a[3]
print(a)

#Delete a slice of the list
a = [1, 9, 8, 10, 3, 4, 5]

#use del
del a[1:3]
print(a)

print(a.remove(10)) # here 10 is value from the list.
print(a.pop(4))  # here 4 is index