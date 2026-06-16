
txt = ['1','2','3','4']
with open(r'Data\output.txt', mode = 'a',encoding='utf-8') as data:
    for i in txt:
        data.write(i+ '\n')