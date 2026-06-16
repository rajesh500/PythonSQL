nums = [6,6,2,3,3,4,4,8,8]

dit = {}
for i in nums:
    if i in dit:
        dit[i]=dit[i]+1
    
    else:
        dit[i]=1
    #print(dit)

#print(dit)
print(dit.keys())
print(dit.values())

if 1 in dit.values():
    #print(dit[1])
    print("yes")
    
for j, k in dit.items():
    #print(j)
    if k==1:
        print(j)
        
'''
a = 0
m = 1
b = 2
for i in range(1, len(nums)-1):
    if nums[a] == nums[m] or nums[m] == nums[b]:
        print("matching")
    else:
        print("not matching")
    a = a + i
    m = m + i
    b = b + i 
    
    '''


'''      
a=0
m=1
list_dup = []
list_nondup = []
for i in range(1, len(nums)):
    if nums[a] == nums[i]:
        list_dup.append(nums[a])
    else:
        list_nondup.append(nums[i])
    #print(i)
    a=a+1
print(list_dup)
print(list_nondup)

 '''
