test_str = "geeksforgeeks is best for geeks. A geek should take interest."
que_word = "geek"

count = 0
i = 0
d = {}
while i < len(test_str):
    str_form = test_str[i:i+len(que_word)]
    if que_word == str_form:
        count = count + 1
        if str_form in d:
            d[str_form] =   count
        else:
            d[str_form] = count
    i = i+1

# converting dictionary key value to string 
key, value = list(d.items())[0]
print('key', key)
print('value', value)

# Approach-2
print(test_str.count(que_word))