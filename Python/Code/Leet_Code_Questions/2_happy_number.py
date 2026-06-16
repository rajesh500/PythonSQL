
# def square_cal(n):
#     ss = 0
#     while n !=0:
#         ss = ss + (n %10) * (n%10)
#         #print('ss', ss)
#         n = n//10
#         #print('n', n)
    
#     return ss


# def happy_number(n):
#     s = set()
#     a = True
#     while a:
#         #print('Iteration')
#         n = square_cal(n)
#         #print(n)
#         if n == 1:
#             a = False
#             print('True')
#         if n in s:
#             print('False')
#         s.add(n)
#     print('s', s)
    
# print(happy_number(19))
    




def happy_number(n):
    while (1):
        total = 0
        while n != 0:
            mul_val = (n%10)*(n%10)
            total = total + mul_val
            n = n//10
        n = total 
        if n == 1:
            return True
    return False



res = happy_number(19)
print(res)




















 



# def numSquareSum(n):
#     squareSum = 0
#     while (n != 0):
#         squareSum += (n % 10) * (n % 10)
#         print(squareSum)
#         n = n // 10
#         print(n)
#     return squareSum

# a = numSquareSum(82)
# print(a)