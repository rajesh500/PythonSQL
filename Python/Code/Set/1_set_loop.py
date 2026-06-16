#types of loops in set.
#for loop same but behind for loop it will call __iter__() methods for looping.
# in set we can directly call this __iter__() method.
# order is not gauranty 
a = set("geEks")
for i in a.__iter__():
    print(i)


# max and min values:
s1 = {4, 12, 10, 9, 4, 13}
print(min(s1), 'min')
print(max(s1), 'max')

sorted_d = sorted(s1)
print(sorted_d[0], 'min')
print(sorted_d[-1], 'max')


