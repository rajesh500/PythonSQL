str =" geeks quiz practice code"
split = str.split()
print(split)

# logic approach
l = []
i = len(split)-1
while i >= 0:
    l.append(split[i])
    i= i-1

print(' '.join(l))

#approach2 simply with in split level.
split = str.split()[::-1]
print(' '.join(split))


# Approach3
split = str.split()[::-1]
ll = []
for i in split:
    ll.append(i)
print(' '.join(l))

# Approach 4 with methods.
str =" geeks quiz practice code"
print(' '.join(reversed(str.split())))


# AP-5
str_split = str.split()
x = [str_split[i] for i in range(len(str_split)-1, -1, -1)]
print(x)