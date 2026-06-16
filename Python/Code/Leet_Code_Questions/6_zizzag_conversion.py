s = "PAYPALISHIRING"
numRows = 3
# 0 1 2 1 0 1 2 1 0 1 2 1 0 1

rows = [[] for i in range(numRows)]
index = 0
step = 1
for i in s:
    print(index,  end= ' ')
    rows[index].append(i)
    if index == 0:
        step = 1
    elif index == numRows - 1:
        step = -1
    index = index + step
    print(index, 'index')

strr = ''
for j in range(numRows):
    strr += ''.join(rows[j])
print(strr)