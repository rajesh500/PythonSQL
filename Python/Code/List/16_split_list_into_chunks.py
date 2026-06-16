# spliting the list size into those chunks
# chunks size need to define.
# yield keyword terminate the loop once condition satisfied and below line of yield code will not execute.
data = list(range(10))
n= 3
for i in range(0, 10, 3):
    print(data[i:i+n])
