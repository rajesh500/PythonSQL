s1 = "Geeks for Geeks"
s2 = s1.split()

# AP-1
# print(list(set(s2)))
# print(' '.join(list(set(s2))))


## AP-2
# d = {}
# count = 1
# for i in s2:
#     if i in d:
#         d[i]= d[i]+count
#     else:
#         d[i] = 1

# dup_str = ''
# for k, v in d.items():
#     if v > 1:
#         dup_str = k

# s2.remove(dup_str)
# print(' '.join(sorted(s2)))


# AP-3:
# creating a dictionary from string, string values are going to be keys and value will be None.
# here keys can't be duplicate hence required out will return .

print(' '.join(list(dict.fromkeys(s2))))
