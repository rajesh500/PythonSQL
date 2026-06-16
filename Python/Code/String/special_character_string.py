#str = 'Geeks$For$Geeks'
str = 'GeeksForGeeks'
# import re

# regex = re.compile('[$]')
# if regex.search(str) == None:
#     print("string")
# else:
#     print("not accepted")


#Apporach2 
str2 = 'Geeks$For$Geeks'
s = '[@_!#$%^&*()<>?/\|}{~:]'
count  = 0
for i in str2:
    if i in s:
        print(i)
        count +=1

if count == None or count == 0:
    print("String accepted")
else:
    print("string not accepted")


# #approach3:
# str3 = 'Geeks$For$Geeks'
# count3 = 0
# for i in str3:
#     if i.isalpha() or i.isdigit():pass
#     else:
#         count3 = count3+1

# if count3 == None or count3 ==0:
#     print('String accepted')
# else:
#     print('String not accepted')
