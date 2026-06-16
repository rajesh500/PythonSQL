from itertools import permutations

pl = list(permutations('ABC'))
for i in pl:
    print(''.join(i))