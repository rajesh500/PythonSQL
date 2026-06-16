a = [1,2,3,4,5,6,7,8,9]
# c = [1,2,3,4,5,6,7,8,9]
# b=a
# b.reverse()
# print("list reverse method", b)
# print(c[::-1])

# for i in range(len(a)-1, -1, -1):
#     print(a[i])

# b=[]
# for i in a:
#     b=[i]+b
#     print(b)

# print(b)

c=[]
for i in range(1, 10):
    #print(len(a)-i, j)
    c.insert(i, a[len(a)-i])
print(c)