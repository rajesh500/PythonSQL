data = [2,4,5,6,1,2,6,8,9,20, 21,50, 23,56]

even_count = 0
odd_count = 0

for i in data:
    if i%2==0:
        even_count +=1
    else:
        odd_count +=1
    

print('even', even_count)
print('odd', odd_count)