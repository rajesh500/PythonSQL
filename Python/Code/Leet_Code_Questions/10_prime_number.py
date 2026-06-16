n = 10
for num in range(n):
    if num > 1:
        for i in range(2, num):
            if num%i==0:
                break 
        else:
            print(num)

# n = 10
# empt_list = []
# for j in range(1, n+1):
#     #print(j, 'j')
#     if j <= 1:continue
#     if j == 2:
#         empt_list.append(2) 
#     if j % 2 == 0:
#         #print(j, 'break')
#         continue
#     a=0
#     for i in range(3, j, 2):
#         #print(i, 'i')
#         if j%i == 0:
#             a = a+1
#             break
#     if a == 0:
#         empt_list.append(j)
# print(empt_list)




# import math

# def is_prime(number):
#     if number <= 1: return False
#     if number == 2: return True
#     if number % 2 == 0: return False
#     # Check odd divisors up to sqrt(n)
#     print(math.sqrt(number))
#     for i in range(3, int(math.sqrt(number)) + 1, 2):
#         print(i)
#         if number % i == 0: return False
#     return True

# # Example
# print(is_prime(17))

# # for i in range(3, 15, 2):
# #     print(i)