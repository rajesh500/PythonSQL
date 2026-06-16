def scoreBalance(s: str):
    total = 0
    subtotal = 0
    for i in s:
        total = total + ord(i)-96
    print(total)
    for j in s:
        print(j)
        subtotal = subtotal + ord(j)-96
        print(subtotal)
        if subtotal == (total - subtotal):
            return True
    return False

res = scoreBalance('fcab')
print(res)



# l1 = 0
#         r2 = len(s)-1
#         d={'a':1,'b':2, 'c':3, 'd':4}
#         left_total = 0
#         right_total = 0
#         for i in range(len(s)):
#             left_sub = s[l1:i+1]
#             right_sub = s[(i+1):r2+1]
#             print(left_sub, right_sub)
#             for i in left_sub:
#                 left_total = left_total + d.get(i, 0)
#                 print(left_total)
#             for j in right_sub:
#                 right_total = right_total + d.get(j, 0)
#                 print(right_total)
#             if left_total == right_total:
#                 return True
#                 break
#             left_total =0
#             right_total =0
#         return False