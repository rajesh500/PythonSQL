dict = {'a':1, 'b':2, 'c':4}

#print(dict['d'])   # if key is not in the dictionary, then it will return KeyError: 'd'

# ---- 1----
#print(dict.get('d', 'Not Found'))


try:
    print(dict['d'], 'expected value')
except KeyError as e:
    print(e)


if 'e' in dict:
    print(dict['e'])
else:
    print('key not found')