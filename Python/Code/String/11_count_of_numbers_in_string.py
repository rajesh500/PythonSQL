test_str = "geeks4feeks is No. 1 4 geeks"

count = 0
for i in test_str:
    if i.isnumeric():
        count = count + 1

print("Count of numerics in string :", count)


dcount = 0
for i in test_str:
    if i.isdigit():
        dcount = dcount + 1

print("Count of numerics in string :", count)