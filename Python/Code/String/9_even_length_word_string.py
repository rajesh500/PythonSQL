# even strings
# AP-1
str = "This is a python language"

split_str = str.split()
emp_list = []
for i in split_str:
    if len(i)%2==0:
        emp_list.append(i)

# print(' '.join(emp_list))

# # lambda function
# #lambda argument:expression
# s= lambda x:len(x)%2==0
# print(s('this'))

# # even number from list
# def is_multiple(sum):
#     return sum%10==0

# # filter(expression, sequence)
# s2 = [1,2,3,10, 20]
# s1 = list(filter(lambda x:is_multiple(x), s2))
# print(s1)

# # even numbers:
eve = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20] 
# eve_check = list(filter(even_check(), eve)) -- will not work
eve_check = list(filter(lambda x: x%2==0, eve))   # lambda need to be used
print(eve_check)


# def even_check(num):
#     if num == 6 or num == 8:pass
#     elif num ==12:
#         num = num/3
#         return num%2==0
#     else:
#         return num%2==0
    
# # eve_check = list(filter(even_check(), eve)) -- will not work
# eve_check = list(filter(lambda x: even_check(x), eve))   # lambda need to be used
# print(eve_check)