string = "14, 625, 498.002"
str1 = string.replace('.', 'ttt')
str1 = str1.replace(', ', '.')
str1 = str1.replace('ttt', ', ')
print(str1)