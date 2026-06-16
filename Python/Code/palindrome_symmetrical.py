#palindrome approach
def is_palindrome(s):
    return s == s[::-1]

#symmetrical apporach, works for even length strings only.
def is_symmerical(s):
    mid = int(len(s))
    if mid%2 ==0:
        m = mid//2
        print('left', s[:m], 'right', s[m:])
        return s[:m] == s[m:]

str='madam'      #'amaama'
# check what function is returning ## it is returning boolean value
b = is_palindrome(str)
print('b', b)
if is_palindrome(str):
    print("This is palindrome")
else:
    print("This is not palindrome")
# function is returning none    
a=is_symmerical(str)
print('a', a)
if is_symmerical(str):
    print("This is symmetrical")
else:
    print("This is not symmetrical")