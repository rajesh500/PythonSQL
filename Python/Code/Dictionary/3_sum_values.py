d = {'a':100, 'b':200, 'c':300, 'd':400}
res = sum(d.values())
print(res)

list_value = d.values()
print(list_value)


from functools import reduce
res = reduce(lambda x, y:x+y, list_value)
print(res, 'reduce')


lcom = sum( i for i in d.values())
print(lcom, 'lcom')


val = 0

for i in d.values():
    val = val + i

print(val, 'val')

