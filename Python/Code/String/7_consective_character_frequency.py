test_str = 'geekforgeeekssss is bbbbest forrrr geeks'

K = 4 
# str_add =''
# empt_list = []
# for i in range(len(test_str)-1):
#     if test_str[i] == test_str[i+1] and test_str[i] == test_str[i+2] and test_str[i]== test_str[i+3]:
#         print(i)
#         empt_list.append(test_str[i:i+4])

# print(empt_list)

#Approach2 dynamic way
secchar = None
count = 1
l = []
for i in test_str:
    if i == secchar:
        count = count + 1
    else:
        secchar = i
        count = 1
    if count == K:
        l.append(K*i)
    
print(l)


