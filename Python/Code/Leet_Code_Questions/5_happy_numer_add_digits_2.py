# def addDigits(num):
#     total = 0
#     while num != 0:
#         a = num%10
#         #print('a', a)
#         total = total + a
#         #print('total', total)
#         num = num//10
#         #print('num', num)
#     return total
    
# def add_digits(n):
#     while (1):
#         print('n1', n)
#         n = addDigits(n)
#         if n <= 9:
#             return n

# a = add_digits(38)
# print(a)

## ***** note instead of writing two functions and two loop we can handle in one loop and one function.

# def addDigits(num):

#     while num>=10:
#         total = 0
#         while num>0:
#             a = num%10
#             total = total + a
#             num = num//10
#         num = total
#     return num

# res =  addDigits(381)
# print('res', res)



def addDigits(num):
    while (1):
        total = 0
        while num>0:
            a = num%10
            print(a, 'a')
            total = total + a
            print(total,'total')
            num = num//10
            print(num, 'num1')
        num = total
        print(num, 'num2')
        if num <=9:
            return num
    return num

res =  addDigits(129)
print('res', res)