s = 'xyyz'   # delete one y only
emp_list  = []
for i in s:
    if i in emp_list:
        pass
    else:
        emp_list.append(i)

print(''.join(emp_list))