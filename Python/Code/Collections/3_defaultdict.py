from collections import defaultdict

d = defaultdict(list)

d['apple'].append('fruit')
d['carrot'].append('vegetable')
print(d)
#print(d['banana'])

d1 = defaultdict(str)

d1['apple_str'] = 'fruit'
d1['carrot_str'] = 'vegetable'
print(d1, 'd1')
#print(d1['banana'])   # empty string return 


d2 = defaultdict(int)
for i in range(5):
    d2[i] = d2[i]+ 10

print(d2, 'd2')
#print(d2[5])   # return 0 

# list, str, int are default_factory 



#####   -----------------------------------------

'''
words = ["apple", "ant", "banana", "bat", "carrot", "cat"]
d = {}
char_list = []
empt_list = [[]]
for word in words:
    if word[0] in char_list:
        pass
    else:
        char_list.append(word[0])

# empt_list2 = empt_list * len(char_list)
# print(empt_list2, '2')
empt_list = [[] for _ in range(len(char_list))]  # FIXED
print(empt_list, '1')

print(char_list)
for sword in words:
        print(sword[0])
        for itr, chr in enumerate(char_list):
             print('itr', itr, 'chr', chr)
             if chr == sword[0]:
                  print(sword)
                  empt_list[itr].append(sword)


    
print(empt_list)



d = {}

for i in range(len(char_list)):
     d[char_list[i]] =  empt_list[i]

print(d)
     


dwords = ["apple", "ant", "banana", "bat", "carrot", "cat"]
from collections import defaultdict

dd = defaultdict(list)
print('dd', dd)

for i in dwords:
     dd[i[0]].append(i)

print(dd) '''