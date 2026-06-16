# subset is sequence of element in a set.
# Example: f we have s = {1, 2, 3, 4} and need to find subsets of size k = 2, the output should be [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)].

# using itertools.combinations can generate subset.

from itertools import combinations
s = {1, 2, 3, 4}
k = 2

subsets = list(combinations(s, k))
print(subsets)


# Brute force
ss = []
for i in s:
   # print(i)
    for j in range(i+1, len(s)+1):
        a = [i, j]   # list of list
        #a = (i, j)  # list of tuple
        #print(i, j, end = " ")
        if len(a) == 2:
            ss.append(a)

print(ss)


