# String reverse using method.
my_str = 'Python World'
#print(''.join(reversed(my_str)))

# String reverse using slicing
#print(my_str[::-1])

#using loop
empty_str = ''
for i in range(1, len(my_str)+1):
    print(my_str[-(i)])
    empty_str = empty_str+my_str[-(i)]
print(empty_str)    


