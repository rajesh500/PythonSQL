d = {'alleged': ['truths', 'fiels', 'fact', 'infidelity', 'incident'],
 'greased': ['axle', 'wheel', 'wheels', 'fields', 'enGine', 'pizza'],
 'plowed': ['fields', 'field', 'field', 'incident', '', '']}


d_find_and_replace = {'wheels':'wheel', 'Field': 'field', 'enGine':'engine', 'axle':'AXLE'}

import copy
c = copy.deepcopy(d)
# print(c)

for key, value in c.items():
    for i, j in enumerate(value):
        #print(value[i])
        print(d_find_and_replace.get(value[i]))
        if d_find_and_replace.get(value[i]):
            value[i] = d_find_and_replace.get(value[i])

print(c)
