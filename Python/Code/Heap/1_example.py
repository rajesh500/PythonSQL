import heapq

a = [2,3,45,0,1]
heapq.heapify(a)
print(a)

# min-heap
heapq.heappop(a)
print(a)

# max-heap
b = [1,2,3,4,6,5]
max_heap = [-x for x in b]
heapq.heapify(max_heap)
print(max_heap)
print(-heapq.heappop(max_heap))   


maxi = heapq.nlargest(3, a) 
print(maxi)
mini = heapq.nsmallest(3, a)
print(mini)

aa = [(2, "Task A"), (1, "Task B"), (3, "Task C"), (5, "Task D"), (4, "Task E")]
maxi = heapq.nlargest(3, aa, key = lambda x:x[0])
print(maxi)
mini = heapq.nsmallest(2, aa, key = lambda x:x[0])
print(mini)


h1 = [10, 20, 15, 30, 40]
heapq.heapify(h1)
min = heapq.heapreplace(h1, 5)
print(min)
print(h1)
h2 = [2,4,6,8]
h3 = list(heapq.merge(h1, h2))
print(h3)