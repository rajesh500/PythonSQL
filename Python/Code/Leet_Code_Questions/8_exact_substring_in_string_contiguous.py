from collections import Counter

a = [1, 2, 2, 2, 3]
b = [2, 2, 2, 4]

print(Counter(a))
print(Counter(b))
c = Counter(a) & Counter(b)
print(c)
print(list(c.elements()))
inter = list((Counter(a) & Counter(b)).elements())
#print(inter)

''' explanation'''
'''
With:

a = [1, 2, 2, 3] → counts are {1: 1, 2: 2, 3: 1}
b = [2, 2, 2, 4] → counts are {2: 3, 4: 1}

What each part does

Counter(a) and Counter(b) build frequency maps (value → how many times it occurs).
Counter(a) & Counter(b) computes the intersection by taking, for each value present in both, the min count:

For 2: min(2, 3) = 2
1 isn’t in b, 4 isn’t in a, so they drop out
Result is effectively {2: 2}


.elements() turns that Counter back into an iterator that yields values repeated by their count:

{2: 2} → yields 2, 2


list(...) materializes it as [2, 2].
'''