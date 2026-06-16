test_dict = {'gfg' : {'Manjeet' : 5, 'Himani' : 10},
             'is' : {'Manjeet' : 8, 'Himani' : 9},
             'best' : {'Manjeet' : 10, 'Himani' : 15}}

#print(test_dict['gfg']['Manjeet'])
# # Ap-1
# largest = 0
# for k, v in test_dict.items():
#     for k1, v1 in v.items():
#         #print('k1', k1, 'v1', v1)
#         if  largest < v1:
#             largest = v1
# print(k, largest)


# # AP-2:
# key = 'Himani'    # search key is fixed.
# largest = 0
# for k, v in test_dict.items():
#     if largest < test_dict[k][key]:
#         largest = test_dict[k][key]
# print(k, largest)

# Ap-3
key = 'Himani'
res = max(test_dict, key = lambda sub: test_dict[sub][key])
res_min = min(test_dict, key = lambda sub: test_dict[sub][key])
print(res)

