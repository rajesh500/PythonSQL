data = [2,4,5,6,1,2,6,8,9, 2, 4, 3, 1, 2]

d={}

for i in data:
    if i in d:
        d[i]= d[i]+1
    else:
        d[i]= 1

print(d)

sorted_dict_desc = dict(sorted(d.items(), reverse=True))
print(sorted_dict_desc)

# srt_keys = sorted(d)
# print(dict(srt_keys))


# AP-2
# from collections import Counter
# c = Counter(data)
# print(c)