from collections import Counter
Inpute = [ "john", "johnny", "jackie", "johnny", "john", "jackie", "jamie", "jamie", "john", "johnny", "jamie", "johnny", "john" ]

res = Counter(Inpute)
print(res)

m = max(res.values())
print('m', m)
smallest = ''
largest = 100
win = ''
for key, value in res.items():
    if  value == m:
        if    largest >  len(key):
            smallest = key
            largest = len(key)
print(smallest)
