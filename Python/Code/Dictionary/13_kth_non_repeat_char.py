from collections import Counter, OrderedDict

s = "geeksforgeeks"
k=3

# Ap-1
res = Counter(s)
print(res)

empt = []
for key, value in res.items():
    if value == 1:
        empt.append(key)

print(empt[2:], 'AP1')


# # AP-2    counting characters using OrderedDict()
# freq = OrderedDict()
# for i in s:
#     freq[i]= freq.get(i, 0)+ 1

# empt = []
# for key, value in freq.items():
#     if value == 1:
#         empt.append(key)

# print(empt[2:], 'AP2')

