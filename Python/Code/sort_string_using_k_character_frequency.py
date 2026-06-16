test_list = ["geekforgeekss", "is", "bessst", "for", "geeks"]
k = 's' 
d = {}
for i in test_list:
    d[i] = i.count(k)

# sort dictionary values using key, keys in descending order
e = dict(sorted(d.items(),  key=lambda item: item[1], reverse =  True))
emp_list = []
for k in e:
    emp_list.append(k)

print(emp_list)