test_dict = {"Gfg" : 4, "is" : 7, "Best" : 8, "for" : 6, "Geeks" : 10}

# # AP-1
# value_list = []
# for k, v in test_dict.items():
#     value_list.append(v)

# print(sum(value_list)/len(value_list))


# AP-2
def add(x, y):
    return x + y

value_list = []
for k, v in test_dict.items():
    value_list.append(v)

from functools import reduce
res = reduce(add, value_list)
print(res/len(value_list))
