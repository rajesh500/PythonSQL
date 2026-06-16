data = [2,4,5,6,1,2,6,8,9]
even_list = []
for i in data:
    if i%2==0:
        even_list.append(i)

print(even_list)


#square original list:
new_list = [x**2 for x in data]
print(new_list)