test_str = 'geeksforgeeks is best for geeks'
wrd = 'best' 
str_sp = test_str.split()
if wrd in str_sp:
    print(str_sp.index(wrd)+1) 


for i in str_sp:
    if i == wrd:
        print(str_sp.index(i)+1)
