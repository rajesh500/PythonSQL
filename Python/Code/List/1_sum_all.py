### 1 sum of all elements ###
data = [2,4,5,6,1,2,6,8,9]

sum_data = 0
for i in data:
    sum_data += i
print(sum_data)


## 2 ##
x=0
sum_c = sum([i for i in data])
print(sum_c)

print('sum', sum(data))
