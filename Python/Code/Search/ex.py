data = [56,26,93,17,31,44,44, 2, 26]
data.sort()
print(data)
key = 44
low = 0 
high = len(data)-1
first = None


while low <= high:
    mid = (low + high)//2

    if data[mid] == key:
        first = mid 
        high = mid - 1
    
    elif  data[mid] < key:
        low = mid + 1

    else:
        low = mid + 1

print(first)

'''
it-1:
0<7
mid = 3
26 == 44
26 < 44
low = 4

it-2:
4<7
mid = 5
44 ==44:
first = 5
high = 4

it-3:
4<= 4
mid = 4
31 ==4
31<44
low = 5 

    
it-1:
0<7 
mid = 3
26 == 26
first = 3
high = 2

it-2
0<2
mid = 1
17 < 26
low = 2 

it-3:
2<=2
mid = 2
26 ==26 
first = 2

exit Look


'''