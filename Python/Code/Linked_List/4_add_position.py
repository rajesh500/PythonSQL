class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def traversal_data():
        n = curr 
        while n is not None:
            print(n.data, 'data', n.next, 'nexterence')
            n = n.next

# def add_element(data):
#      NewNode = Node(data)
#      NewNode.next = curr     # here curr is nothing but node1
#      return NewNode         # returning newnode
     
# def add_end(data):
#     endNode = Node(data)
#     # if curr is None:
#     #      curr = endNode
#     #      return endNode
#     last = curr
#     while last.next is not None:
#         last = last.next 
        
#     last.next = endNode
#     return endNode


def add_position(curr, data, pos):
    posNode = Node(data)

    for i in range(0, pos-1):    # iteration once but curr.next hit it will go to 15 node.
        
        curr = curr.next
        print('pos', curr)
    
    print('current', curr.next)
    posNode.next = curr.next
    curr.next = posNode
    return posNode


if __name__ == '__main__':
    curr = Node(10)
    curr.next = Node(15)
    curr.next.next = Node(20)
    curr.next.next.next = Node(18)
    add_position(curr, 16, 2)
    traversal_data()


