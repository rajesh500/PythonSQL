data = [2,4,5,6,1,2,6,8,9]

dup = []
original = []
for i in data:
    if i in original:
        print(i)
        dup.append(i)
    else:
        original.append(i)

print('dup', dup)
print('original', original)


print(list(set(data)))