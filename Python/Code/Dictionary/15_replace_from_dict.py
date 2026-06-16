s = "hello world, have a great day"

r_dict = {"hello": "hi", "world": "earth", "great": "wonderful"}


# AP-1
# for key, value in r_dict.items():
#     s= s.replace(key, value)

# print(s)



#AP-2:

res = ' '.join(map(lambda word: r_dict.get(word, word), s.split()))
print(res)
