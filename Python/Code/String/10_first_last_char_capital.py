str = 'welcome to geeksforgeeks'
str_splt = str.split()
empt_str = []
for i in str_splt:

    first_char = i[:1]
    mid_char = i[1:len(i)-1]
    last_char = i[len(i)-1:]

    empt_str.append(first_char.upper() + mid_char + last_char.upper())

print(' '.join(empt_str))
    
