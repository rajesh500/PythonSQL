str = "hello geeks for geeks"
str_split = str.split()
k = 4
empt_str = ''
for i in str_split:
    if len(i) > k:
        empt_str += i + ' '

print(empt_str)

#Apprach2:
m = 4
lamda_ap = list(filter(lambda x:(len(x) > m), str_split))
print(lamda_ap)
