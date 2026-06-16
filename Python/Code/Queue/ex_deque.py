from collections import deque

data = [10, 20, 40, 60, 30, 100, 80]
dq = deque(data)
print(dq)
print(dq[0])   # Accessing / Index accessing

dq.append(200)
print(dq)

dq.appendleft(250)
print(dq)

dq.pop()
print(dq)

dq.popleft()
print(dq)

cust_data = [550, 1200, 900]
dq.extend(cust_data)
print(dq)

dq.extendleft(cust_data)
print(dq)

dq.remove(1200)   # remove from front.
print(dq)

dq.reverse()
print(dq)

print(dq.count(550))
print(dq)


dq.rotate(3)    # last 3 elements move to front.
print(dq)


dq.rotate(-2)    # first 2 elements move to end.
print(dq)        