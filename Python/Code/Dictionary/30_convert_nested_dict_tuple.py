d = {'gfg': {'x': 5, 'y': 6}, 'is': {'x': 1, 'y': 4}, 'best': {'x': 8, 'y': 3}}


from collections import defaultdict

dd = defaultdict(tuple)
# print(dd)

for k, v in d.items():
    for key, value in v.items():
        #print(key, value)
        dd[key] = dd[key] + (value, )

print(dd.items())