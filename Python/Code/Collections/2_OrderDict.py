from collections import OrderedDict

od = OrderedDict()
od['key'] = 1
od['chian'] = 2
od['lock'] = 3

#print(od)


#for k, v in od.items():
    #print('k', k, 'v', v)

a = [('a', 1), ('b', 2), ('c', 3), ('d', 4)]
od2 = OrderedDict(a)
# print('od2', od2)


print('od2', OrderedDict(reversed(list(od2.items()))))
od3 = OrderedDict(reversed(list(od2.items())))
print(od3, 'od3')
od3.move_to_end('d')
print(od3)

# for k, v in od3.items():
#     print(k,v)


res = od3.popitem(last=True)  # last element remove
res = od3.popitem(last=False)  # First element remove
#print('res', res)
#od3.pop('a')   # delete item

# od3.move_to_end('d') # here a is key    * move to Last 
# #res.move_to_end('a') # move to first/front.
# print('od3-2', od3)