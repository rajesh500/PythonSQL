# def checkstring(str):
#     alpha=False
#     num = False
#     for i in str:
#         if i.isalpha():
#             alpha = True
#         if i.isnumeric():
#             num = True 
#     return alpha,  num


# a, b = checkstring('welcome3G')
# if a == True and b == True:
#     print('True')
# else:
#     print('False')



a = 'welcome3G'
if a.isalnum():
    print('True')
else:
    print('False')
