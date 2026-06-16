d1 = {'x': 1, 'y': 2}
d2 = {'y': 3, 'z': 4}


d3 = d1 | d2
print(d3, 'd3')



# d1.update(d2)
# print(d1, 'update')


d4 = d1.copy()
print(d4, 'shallow copy')

for key, values in d2.items():
    d4[key] = values

print(d4, 'd4')
print(d1, 'd1')