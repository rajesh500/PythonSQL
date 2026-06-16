test_str = "GeeksforGeeks"

d={}
for i in test_str:
    if i in d:
        d[i] = d[i]+1
    else:
        d[i]=1

    large_value = 0    
    if d[i] > large_value:
        large_value = d[i]
        large_key = i

print(d)     ## till here last character is s because of it is returning 2 but if think of character wise below solution is good. 
print('key',large_key, 'value', large_value)

new_dict = {}
for k, v in d.items():
    if v > 1:
        new_dict[k]=v

print(new_dict.get(max(list(new_dict.keys()))))

# large_value = 0

# for i in d:
#     if d[i] > large_value:

#         large_value = d[i]
#         large_key = i


