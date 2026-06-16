test_list = ['geeksforgeeks is best for geeks']
chr_list = ['e', 'b', 'g', 'f'] 
str = ''.join(test_list)                                                             
d = {}

for i in test_list[0]:
    if i.isspace():pass
    else:
        if i in d:
            d[i] = d[i]+1
        else:
            d[i] =1


# out = {}
# for j in chr_list:
#     print(d[j])
#     out[j] = d[j]

# print(out)
out = {}
for j in chr_list:
    out[j] = d.get(j)

print(out)
