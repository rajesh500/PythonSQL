my_dict = {'apple': 10, 'banana': 3, 'cherry': 7, 'key': 1}

st = dict(sorted(my_dict.items(),   key = lambda item:item[1]))
print(st)


key = lambda item:item[1]
print(key)