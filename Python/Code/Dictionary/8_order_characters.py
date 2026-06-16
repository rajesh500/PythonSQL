# s = 'engineers rock'
# pattern = 'er'

# last_char = pattern[-1:]
# first_char = pattern[:len(pattern)-1]
# print(first_char)
# char_index = []
# for i, j in enumerate(s):
#     if j ==last_char:
#         char_index.append(i)
# print(char_index)


# for m, n in enumerate(s):
#     if n==first_char and 


# from collections import OrderedDict

# s = 'engineers rock'
# p = 'er'

# od = OrderedDict()
# for i, ch in enumerate(s):
#     if ch not in od:
#         od[ch] = i

# print(od)
# pos = -1
# for ch in p:
#     if ch not in od or od[ch] < pos:
#         print(False)
#         break
#     pos = od[ch]
# else:
#     print(True)


# First Occurance 
# s = 'engineers rock'
# p = 'er'

# ind = 0
# d = {}
# for i in s:
#     if i in d:
#         pass
#     else:
#         d[i]= ind
#         ind = ind + 1

# first_char = p[:len(p)-1]
# print('first_char', first_char)
# last_char = p[-1:]
# print('last_char', last_char)

# if d[first_char] < d[last_char]:
#     print('True')
# else:
#     print('False')


# Last Occurance of each character.
ud = {}
rd = {}
s = 'engineers rock'
p = 'er'

for i, j in enumerate(s):
    if j in ud:
        rd[j]=i
    else:
        ud[j]= i

print('UD', ud)
print('RD', rd)


first_char = p[:len(p)-1]
print('first_char', first_char)
last_char = p[-1:]
print('last_char', last_char)


if rd[first_char] < rd[last_char]:
    print('True')
else:
    print('False')
