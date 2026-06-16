from collections import Counter 

ar1 = [1, 5, 10, 20, 40, 80]
ar2 = [6, 7, 20, 80, 100]
ar3 = [3, 4, 15, 20, 30, 70, 80, 120]


ac1 = Counter(ar1)
ac2 = Counter(ar2)
ac3 = Counter(ar3)
print('ac1', ac1)
print('ac2', ac2)
print('ac3', ac3)


ac_dict_intersection = dict(ac1.items() & ac2.items() & ac3.items())    # intersection in dictionary
print('aci', ac_dict_intersection)

ac1.update(ac2)
ac1.update(ac3)

mc = ac1.most_common(2)
ec= []
for i in mc:
    ec.append(i[0])

print(sorted(ec, reverse=True))


