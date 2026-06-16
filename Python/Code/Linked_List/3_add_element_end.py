class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None

def traversal_data():
        n = head 
        while n is not None:
            print(n.data, 'data', n.ref, 'reference')
            n = n.ref

def add_element(data):
     NewNode = Node(data)
     NewNode.ref = head     # here head is nothing but node1
     return NewNode         # returning newnode
     
def add_end(data):
    endNode = Node(data)
    # if head is None:
    #      head = endNode
    #      return endNode
    last = head
    while last.ref is not None:
        last = last.ref 
        
    last.ref = endNode
    return endNode

if __name__ == '__main__':
    head = Node(10)
    head.ref = Node(15)
    head.ref.ref = Node(20)
    head.ref.ref.ref = Node(18)
    add_end(25)
    head = add_element(5)     # assigining newnode as head
    traversal_data()