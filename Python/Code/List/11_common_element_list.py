data1 = [2,4,5,6,1,2,6,8,9]
data2 = [2,3,5,8,10,11,5,6, 1,4,7,9]

print(set(set(data1) & set(data2)))


if len(data1) < len(data2):
    main_dataset = data1

else:
    main_dataset = data2

common = []
for i in set(main_dataset):
    if i in set(data2):
        common.append(i)

print('common: ', common)

