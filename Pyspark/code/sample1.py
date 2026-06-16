
import pandas as pd
dataA = [(21,), (54,), (34,), (45,), (47,), (90,), (100,)]
dataB = [('A',), ('B',), ('C',), ('K',), ('E',), ('F',),('G',)]

df1 = pd.DataFrame(dataA)
df2 = pd.DataFrame(dataB)
#print(df1)
#print(df2)
empt_list = []

for i in range(0, 1):
    print(dataA[i])

for index, j in enumerate(dataB):
    print(str(j).replace(',', '').replace('(', '').replace(')', ''))
    for i in range(0, index):
        print(dataA[i])
    

