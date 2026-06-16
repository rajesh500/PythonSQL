nums = [2,7,11,15]
#nums = [3,2,4]
#nums = [-3,4,3,90]
target = 0
relist=[]
b=(len(nums)-1)
for i in range(0, 1):
    print("i value", nums[i])
    for j in (1, b):
        print("j value",  nums[j])
        if nums[i]+nums[j]==target:
            print("inside")
            relist.append(i)
            relist.append(j)
            #return(i, j)

print(relist)