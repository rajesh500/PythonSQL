# import heapq
# def min_heap(arr):
#     heapq.heapify(arr)
#     n = len(arr)
#     new_list = [0] * n
#     for i in range(n):
#         minn = heapq.heappop(arr)
#         new_list[i] = minn
#     return new_list

# res = min_heap([1,3,5,7,9,0,2,6,4,8])
# print(res)



import heapq
def max_heap(arr):
    heap_arr = [-x for x in arr]
    heapq.heapify(heap_arr)
    n = len(arr)
    new_list = [0] * n
    for i in range(n):
        maxx = -heapq.heappop(heap_arr)
        new_list[i] = maxx
    return new_list

res = max_heap([1,3,5,7,9,0,2,6,4,8])
print(res)