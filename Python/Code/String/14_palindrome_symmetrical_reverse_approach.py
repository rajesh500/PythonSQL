s = 'amaama'

print(reversed(s))
if s == ''.join(reversed(s)):
    print('it is palindrome')
else:
    print('it is not palindrome')

