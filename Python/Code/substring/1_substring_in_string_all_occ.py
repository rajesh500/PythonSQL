def all_occurance(s, p):
    newList = []
    start = 0
    while True:
        i = s.find(p, start)
        print(i, 'i')
        if i == -1:
            return newList
        newList.append(i)
        print(newList,'newList')
        start = i+1
        print(start, 'start')

#res = all_occurance('aaaa', 'aa')
res = all_occurance('banana', 'ana')
print(res)