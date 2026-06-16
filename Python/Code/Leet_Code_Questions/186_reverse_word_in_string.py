s = ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
s.reverse()
s.insert(len(s)+1, ' ')
print(s)
n = len(s)
start = 0
for i in range(n):
    if s[i].isspace():
        l = start 
        end = i -1
        r = end 

        while l<r:
            s[l], s[r] = s[r], s[l]
            l = l+1
            r = r-1
        start = i + 1
s.pop()
print(s)




