str1 = 'aabcddekll12@'
str2 = 'bb2211@55k'
empt_str = set()
set_str1 = ''.join(set(str1))
set_str2 = ''.join(set(str2))

for i in set_str1:
    if i in set_str2:
        empt_str.add(i)

print(len(empt_str))


#approach2
print(len(set(str1).intersection(str2)))


#AP3:
str1 = 'aabcddekll12@'
str2 = 'bb2211@55k'

# common characters in both strings
print(set(str1)&set(str2))
