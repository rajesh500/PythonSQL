
# True or False Scenario's:
[], (), {}, None, 0 are consider as false
q = 0
r = []
if q and r:
print('True')
else:
print('False')


# operators:
T and T --> True
F and F --> False
T and F --> False
F and T --> False



list1.append(list1.append(0))
# list1 = [0, None]

list1.append(0)
list1.append()
# will return typeerror because append() is expecting value, were in the above condition it will work.