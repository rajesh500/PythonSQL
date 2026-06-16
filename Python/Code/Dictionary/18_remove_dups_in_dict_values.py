d = {'a': [1, 2, 3], 'b': [3, 4, 5], 'c': [5, 6]}

# AP-1
s = set()
for k, v in d.items():
    for i in v:
        if i in s:
            v.remove(i)
        else:
            s.add(i)

print(d)






