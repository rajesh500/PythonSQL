data = [56, 0, 2, 3, 2, 78, 6, 0]

# The data contains duplicates, and the earlier logic didn’t account for them during sorting. 
# Using a min/max search approach helps resolve this. In this dataset, the value 0 appears multiple times; 
# if you search without specifying a starting position, you’ll always get the index of the first 0. To avoid that, 
# we start each search from the current iteration index—everything before that point is already sorted, 
# so there’s no need to scan it again.

for i in range(len(data)):
    min_val = min(data[i:])
    min_ind = data.index(min_val, i)
    data[i], data[min_ind] = min_val, data[i]
    print(data)


# How it works

# It-1:
# min_val = 0, min_ind = 1
# data[0], data[1] = 0, 56
# [0, 56, 2,3,2,78,6,0]

# It-2:
# min_val = min(data[1:]) --> [56, 2,3,2,78,6,0]  = 0
# min_ind = 6
# data[1],  data[6] = 0, 56
# [0, 0, 2,3,2,78,6,56]

# It-3:
# min_val = min(data[2:]) --> [2,3,2,78,6,56]  = 2
# min_ind = 0
# data[2],  data[0] = 2, 2
# [0, 0, 2,3,2,78,6,56]

# It-3:
# min_val = min(data[2:]) --> [3,2,78,6,56]  = 2
# min_ind = 1
# data[3],  data[0] = 2, 3
# [0, 0, 2,2,3,78,6,56]
# .
# .
# .
# .
