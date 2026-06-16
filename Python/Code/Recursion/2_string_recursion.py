# # Ex-1
# def str_reverse(n):
#     if len(n) == 0:
#         return n
#     else:
#         return str_reverse(n[1:])+n[0]


# n = 'Hello'
# print(str_reverse(n))

# in the string recursion we no need reduce n value how we did in factorial or fibonacci.


# Ex-2
def str_reverse(n, acc =''):
    if len(n) == 0:
        return acc
    else:
        return str_reverse(n[1:], acc= n[0]+acc)


n = 'Hello'
print(str_reverse(n))