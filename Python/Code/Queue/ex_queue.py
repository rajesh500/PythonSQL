from queue import Queue 

q = Queue(maxsize=4)
print(q.qsize())

q.put(1)
q.put(2)
q.put(3)
print(q.qsize())

print(q.full(), "Full")
print(q.empty(), "empty")