ldata = [[5, 6, 7], [8, 3, 2], [8, 2, 1]]
# d = {}
# for i in range(0, len(ldata)):
#     print(ldata[i])
#     d[i+1] = ldata[i]

# print(d)


res = {i+1:ldata[i]  for i in range(len(ldata))}
print('res', res)