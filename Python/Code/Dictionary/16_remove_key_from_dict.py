d = {'a':1, 'b':2, 'c':3, 'd':4}
rem = 'a'

#AP-3:
d.popitem()    # LIFO
print(d)

# AP-2:
print(d.pop(rem))
print(d)


# AP-1
del d[rem]
print(d)

# out: {'b': 2, 'c': 3, 'd': 4}