d = {'G': 2, 'e': 4, 'k': 2, 's': 2, 'f': 1, 'o': 1, 'r': 1}

#print(d.keys())
#print(d.values())

for key, value in d.items():
    print(key, value)


d['z']=26
#print(d)

d['s'] = 18
#print(d)


del d['o']
#print(d)


val = d.pop('e')
#print('val', val)

d['ABCD'] = {'AA':'App', 'BB':'Ban', 'CC':'Cat'}
#print(d)


d['ABCD']['AA'] = 'AA12'
print(d)





#list to dictionary:
#using zip method and dictionary comprehension.

keys= ['a','b','c','d','e','f']
values = [1,2,3,4,5]

myDict = { k:v  for(k,v) in zip(keys, values)}
#print(myDict)


nDict = {i:i*2 for i in values}
#print(nDict)


# ID = [100, 101, 102]
# Marks = [74, 75, 75]

# dictionary key can be integer as well.
# myDictI = { k:v for (k,v) in zip(ID, Marks)}
# print(myDictI)


# Nested comprehension:
nestDict ={x: {y:x+y  for y in values} for x in values}
print(nestDict)
