data = [56, 3, 2, 78, 6, 0]
min_val = min(data)
min_ind = data.index(min_val)
print(min_val, 'min value')
print(min_ind, 'min index')


#data[0], data[min_ind] = min_val, data[0]

# follow either one but after swap 0 index and 
# first_value = data[0]
# data[0] = min_val
# data[min_ind] = first_value

print(data, 'before sort')
print(data, 'after sort')


# ascending order using min()
for i in range(len(data)):
    min_val = min(data[i:])
    min_ind = data.index(min_val)
    data[i], data[min_ind] = min_val, data[i]
    print(data)
print(data)


# descending order using max()
for i in range(len(data)):
    min_val = max(data[i:])
    min_ind = data.index(min_val)
    data[i], data[min_ind] = min_val, data[i]

print(data)
