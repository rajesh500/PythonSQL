# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.ref = None

# # defining node with data
# Node1 = Node(15)
# Node2 = Node(10)
# Node3 = Node(20)
# Node4 = Node(18)


# ## linking the nodes
# Node1.ref = Node2
# Node2.ref = Node3
# Node3.ref = Node4
# # first node has head
# head = Node1

# n = head
# while n is not None:
#     print('data', n.data)
#     print('ref', n.ref)
#     n = n.ref

# # head.data has the data
# # head.ref has the reference
# # in while loop first iteration n is not None mean h has data is 15.
# # in the next iteration n value is changing to reference. *******


# same above code can be written in this way and mainly linking the list.
class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None

def traversal_data():
        n = head 
        while n is not None:
            print(n.data, 'data', n.ref, 'reference')
            n = n.ref

if __name__ == '__main__':
    head = Node(10)
    head.ref = Node(15)
    head.ref.ref = Node(20)
    head.ref.ref.ref = Node(18)

    traversal_data()
    