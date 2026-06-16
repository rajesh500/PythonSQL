s = "PAYPALISHIRING"
numRows = 4
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

for j in rows:
    print(''.join(j), end='')
    