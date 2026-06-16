d = ["go", "bat", "me", "eat", "goal", "boy", "run"]
ch = ['e', 'o', 'b', 'a', 'm', 'g', 'l']
c1 = set(ch)
print(c1)
el = []
for i in d:
    if set(i).issubset(c1):
        el.append(i)
print(el)