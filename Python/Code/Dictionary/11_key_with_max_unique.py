d = {"Gfg": [5, 7, 5, 4, 5], "is": [6, 7, 4, 3, 3], "Best": [9, 9, 6, 5, 5]}

small = 0
key_max = ''
for key, values in d.items():
    print(key, 'set', set(values))
    if len(set(values)) > small:
        small = len(set(values))
        key_max = key
print(key_max)


