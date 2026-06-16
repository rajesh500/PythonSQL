#d = {'John': 10, 'Jack': 9, 'Katty': 15, 'Kim':8, 'Lara':12, 'Tim':16}
d = {'1002':101212141002,  '1004': 101212141004, '1001':101212141001, '1003':101212141003, '1000':101212141000 }

p_keys = list(d.keys())
p_keys.sort()
# pp_keys = sorted(p_keys, reverse=False)
# print(pp_keys)
new_d = {i:d[i] for i in p_keys}
print(new_d)


empt_d = {}
for i in p_keys:
    empt_d[i]= d[i]
print('empt_d', empt_d)



