original = 'abcdefghijklmnopqrstuvwxyz'
revrse = 'zyxwvutsrqponmlkjihgfedcba'

dict1 = dict(zip(original, revrse))
print(dict1)
N = 3
str = 'paradox'
pre_str = str[:3-1]
# print(pre_str)

for i in str[2:]:
    pre_str = pre_str + dict1.get(i)

print(pre_str)