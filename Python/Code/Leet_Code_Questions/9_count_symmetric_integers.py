#low = 1, high = 100
# symmetric means for only even number sum of first half number is equal to sum of last half
low = 1
high = 100
empt_list = []
for i in range(low, high+1):
    #print(i)
    if len(str(i))%2 != 0:
        pass 
    else:
        half = len(str(i))//2
        res1 = 0
        res2 = 0
        #print(half, 'half')
        #print(str(i)[:half])
        for j in str(i)[:half]:
            #print(j)
            res1 = res1 + int(j)
        #print(str(i)[half:])
        for k in str(i)[half:]:
            res2 = res2 + int(k)
        #print(res1, 'res1', res2, 'res2')
        if res1 == res2:
            empt_list.append(i)
            
print(len(empt_list))