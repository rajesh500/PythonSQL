
# EX-1   adding elements using slicing.
def list_sum(n, acc = 0):
    if len(n) ==0:
        return acc
    else:
        return list_sum(n[1:], acc + n[0])


data = [10,9,8,7,6,5,4,3,2,1]
print(list_sum(data), 'EX-1')



# EX-2
def list_sum(n, acc = 1):
    if len(n) ==0:
        return acc
    else:
        return list_sum(n[1:], acc * n[0])


data = [10,9,8,7,6,5,4,3,2,1]
print(list_sum(data), 'Ex-2')

