
from collections import Counter

s = "GeeksforGeeks"
d = Counter(s)

print(d)

e = [key for key, value in d.items() if value > 1]
print(e)


for key, value in d.items():
    if value > 1:
        print(key)