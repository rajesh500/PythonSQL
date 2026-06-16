test_str = "geekksforgggeeks"


prev_char = None
empt_list = []
for i in test_str:
    if i == prev_char:
        count = count + 1
    
    else:
        prev_char = i
        count = 1
    
    empt_list.append(count)

print(empt_list)




