a = [("name", "Emma"), ("age", 25), ("city", "New York")]

print(dict(a))

for k, v in a:
    print(k, 'key', v, 'value')


res = {key: value for key, value in a}
print('res', res)

#using for loop


re = dict(map(lambda x:(x[0], x[1]) , a))
print('re', re)