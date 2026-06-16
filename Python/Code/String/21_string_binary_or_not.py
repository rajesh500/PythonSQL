#str = "01010101010"
str = "geeks101"
return_value = ''
for i in str:
    if i.isdigit() == False:
        return_value = 'No'
        break
    else:
        return_value = 'Yes'
print(return_value)

# Approach with method
def binary_check(s):
    for i in s:
        if i.isdigit() == False:
            return 'No'
            break
        else:
            return 'Yes'
print(binary_check("01010101010"))

