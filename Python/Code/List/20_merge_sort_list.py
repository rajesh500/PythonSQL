data1 = [2,4,5,6,1,2,6,8,9]
data2 = [2,4,5,61,2,5]

new_list = data1 + data2
print(sorted(new_list, reverse=True))



data1.extend(data2)
print(sorted(data1, reverse=False))