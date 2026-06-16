class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None
    
    def print_LL(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            n = self.head 
            while n is not None:
                print(n.data, n.next)
                n = n.next 

    def add(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = newNode


    def add_at_index(self, data, pos):
        node = Node(data)
        if self.head is None:
            self.head = node
        
        if pos == 0:
            node.next = self.head
            self.head = node
            return 
        
        if pos > 1:
            curr = self.head
            for i in range(1, pos-1):
                print('i', i)
                curr = curr.next 
            node.next = curr.next 
            curr.next = node 
            return node

        



LL = LinkedList()
LL.add(15)
LL.add(10)
LL.add(20)
LL.add(30)
LL.add_at_index(40,2)
LL.add_at_index(45,3)
LL.add(50)
LL.add_at_index(5,0)
LL.print_LL()
