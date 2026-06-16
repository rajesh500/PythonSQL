def vowel_check(s):
    str = s.lower()
    vowel = set('aeiou')
    s = set()   # dictionary in the set
    
    for i in str:
        if i in vowel:
            s.add(i)
        else:pass
        
    if len(s) == len(vowel):
       print("Accepted")
    else :
        print("Not Accepted")
 


vowel_check('SEEquoiaL')

# Approach2
string = "SEEquoiaL"
string = string.lower()
vowel_count = [string.count('a'), string.count('e'), string.count('i'), string.count('o'), string.count('u')]
if vowel_count.count(0) > 0:
    print('Not accepted')
else:
    print('Accepted')

#vowel_count.count(0) = 0, if it returns zero then all values exists in the vowel_count


#Approach 3
string = 'geeksforthegeeks'
if len(set(string.lower()).intersection('aeiou')) >=5:
    print('accepted')
else:
    print('not accepted')
#).intersection("aeiou")