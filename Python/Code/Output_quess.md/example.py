# # 1
# q = 0
# r = []
# if q and r:
#     print('True')
# else:
#     print('False')

# # out: both are false then go to else because if statement is for true.


# # 2
# p = (1, 10)
# q = 0
# r = []
# if p or q and r:
#     print('True')
# else:
#     print('False')

# # out: True, because p is true.


# # 3
# p = (1, 10)
# q = 0
# if p and q:
#     print('True')
# else:
#     print('False')


# # 4
# list1 = ['abc', '123']
# for i in list1:
#     list1.append(i)
# print(list1)
# # it becomes infinite loop because of its keep on adding and list every time increasing.


# # 5

# list1 = []
# list1.append(list1.append(0))
# print(list1)



# 6  Design a quiz program with 4 options using dicitionary.
#1. Take each question and options as  string and define key and value as string in the dictionary.
# 2. give an option to user to select the answer. once user selected compare user answer with question value and define the score.

# q1 = """This is a question1 
#         a.one
#         b.Two
#         c.Three """
# q2 = """This is a question2"""
# q3 = """This is a question3"""
# d= {q1 : "a", q2 : "a", q3 : "b"}

# for i in d:
#     print(d[i])


# # 7
# str1 = 'AaBbCcDdEeFf'
# var = "c"
# while var in str1:
#     str1 = str1[:-1]
#     print(str1)
#     print(var, end = " ")

# How it works as 
# str1[0:-1:1]  --> end = end - 1 which is -1-1 = -2
# 0   1   2   3   4   5   6   7   8   9   10   11
# A   a   B   b   C   c   D   d   E   e   F    f
# -12 -11 -10 -9  -8  -7  -6  -5 -4  -3  -2    -1  
# Every iteration one char is not considering hence string is shrinking.
# # out:
# '''AaBbCcDdEeF
# c AaBbCcDdEe
# c AaBbCcDdE
# c AaBbCcDd
# c AaBbCcD
# c AaBbCc
# c AaBbC
# c '''


# 8 
count = 0
for i in range(5):
    while i < 3:
        if i == 1:
            break 
        count = count + 1
        i = i + 1
    else: 
        count = count + 1

else:
    count = count + 20

# out = 43
# else will execute without if statement if else is with in the loop.
# when else is written without if statement and break is thier when break execute iteration won't go into else:
# on regualr iteration i will go into else part in the above condition.