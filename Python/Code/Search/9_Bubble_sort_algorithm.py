# Bubble sort
# need two loop to iterate but swap and comparing happen at one loop only.
# In each iteration large value move to end for the rest of iteration large value should be exclude from the iteration for that
#in second loop range(len(data)-1-i)
# compare two values at a time and if first value is greater than second than swapit for ascending order -- vice versa for descending order.

data = [10,15,4,23,0]

# # Ascending order
# for i in range(len(data)-1):
#     for j in range(len(data)-1):
#         if data[j] > data[j+1]:
#             data[j], data[j+1] = data[j+1],  data[j]
#         print(data)
#     print()
# print(data)



## Descending order 
# for i in range(len(data)-1):
#     for j in range(len(data)-1):
#         if data[j] < data[j+1]:
#             data[j], data[j+1] = data[j+1],  data[j]
#         print(data)
#     print()
# print(data)


# last iteration skipping.
# in the print statement iterations are reducing..

for i in range(len(data)-1):
    for j in range(len(data)-1-i):
        if data[j] > data[j+1]:
            data[j], data[j+1] = data[j+1],  data[j]
        print(data)
    print()
print(data)


# O(n2) iterations....