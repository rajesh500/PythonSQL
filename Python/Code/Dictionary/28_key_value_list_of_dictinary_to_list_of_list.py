a = {'name': 'Alice', 'age': 25, 'city': 'New York'} 
#out  [['name', 'Geeks'], ['age', 25], ['city', 'Geeks']]

#AP-1
empt_list = []
for k, v in a.items():
    subList = [k, v]
    #print(subList)
    empt_list.append(subList)
print(empt_list)


#Ap-2
# List Comphrension:
res = [[k, v] for k,v in a.items()]
print(res)


#Ap-3
# using Map:
resMap = list(map(lambda x: [x[0], x[1]], a.items()))
print(resMap)


# print(list(a.items())) # [('name', 'Alice'), ('age', 25), ('city', 'New York')]
# print(set(a.items())) # {('name', 'Alice'), ('city', 'New York'), ('age', 25)}

# AP-4
resList = list(map(list, a.items()))
print(resList, 'resList')