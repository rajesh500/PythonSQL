numbers = [10, 4, 30, 65, 20]

largest  = 0

for num in numbers:
    if num > largest:
        largest = num 

print(largest)

a = sorted(numbers)
print(a[-1:][0])


print(max(numbers))