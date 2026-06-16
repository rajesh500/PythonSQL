str = "GEEGEEKSKS"
sub_str = "GEEKS"
first_char = sub_str[:1]


for i, j in enumerate(str):
    if j == first_char:
        if sub_str in str:
            newstr = str.replace(sub_str, '')
            print(newstr)
        else:
            print('no')



# for i in range(0, len(str)):
#     if str[i] == first_char:
#         sub_str_len = len(sub_str)
#         if str[i:sub_str_len+i] == sub_str:
#             print(str[i:sub_str_len+i])
#             str.replace(str[i:sub_str_len+i], '')
# print(str)


str = "GEEGEEKSKSGEEKS"
sub_str = "GEEKS"

if sub_str in str:
    sub_position = str.find(sub_str)

for i, char in enumerate(str):
    if char == sub_str[0]:
        sub_remaining_string  = str[:sub_position] + str[sub_position+len(sub_str):]
        print("concat string", sub_remaining_string)
        if sub_str in sub_remaining_string:
            sub_position = sub_str.find(sub_str)
            if sub_position == 0:
                break
            print("sub position", sub_position)


# emp_list = []
# str_sub_list = []
# for i, char in enumerate(str):
#     if char == sub_str[0]:
#         emp_list.append(i)
#         first_iter_str = str[i:i+len(sub_str)]
#         if first_iter_str == sub_str:
#             print('true')
#         else:
#             print('false')
# print(emp_list)  # need one more iterations

# str_position = str.find(sub_str)
# print("str_position", str_position)
# sub_str_len = len(sub_str)



# while str_position > 0:
#     sec_sub_str = str[:str_position] + str[str_position+sub_str_len:]
#     print(sec_sub_str)
#     str_position = sec_sub_str.find(sub_str)
#     print("inside loop", str_position)
#     if str_position ==0:
#         print('True')
#     else:
#         print('False')
    
