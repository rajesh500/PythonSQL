class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DLinkedList:
    def __init__(self):
        self.head = None
    

    def print_LL(self):
        if self.head is None:
            print("Linked list is empty")
        n = self.head
        while n is not None:
            print(n.data, end= "<->")
            n = n.next
        print('None')

    def empty_node(self, data):
        if self.head is None:
            newNode = Node(data)
            newNode.next = None
            newNode.prev = None
            self.head = newNode
        else:
            print("Linked List is not empty")

    def add(self, data):
        newNode = Node(data)
        if self.head is None:
            print("Linked List is Empty")
        
        #n=self.head
        newNode.next = self.head
        self.head.prev = newNode
        self.head = newNode

    # travese the linked list in backward direction
    # linked list in reverse
    def print_reverse(self):
        if self.head is None:
            print("Reverse Linked List is Empty")

        n= self.head
        while n.next is not None:
            n =  n.next
        
        while n.prev is not None:
            print(n.data)
            n = n.prev
        print(n.data)
        
    def add_end(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            print("Linked List is Empty")
        
        n = self.head 
        while n.next is not None:
            n = n.next
        n.next = newNode
        newNode.prev = n

    def add_at_index(self, data, x):
        newNode = Node(data)
        if self.head is None:
            return self.head
        n= self.head
        while n is not  None:
            if n.data==x:
                break
            n = n.next
        newNode.next = n.next 
        n.next = newNode
    
    def delete_at_begin(self):
        if self.head is None:
            return self.head
        if self.head.next is None:
            self.head = None
            print("if their is only one node")
        else:
            self.head = self.head.next
            self.head.prev = None
        
    def delete_at_end(self):
        if self.head is None:
            return self.head 
        if self.head.next is None:
            self.head = None 
        n = self.head 
        while n.next.next is not None:
            print(n.data)
            n = n.next
        n.next = None

    def delete_by_value(self, x):
        if self.head is None:
            print("DLL is Empty")
            return
        # if only one and delete that.
        if self.head.next is None:
            if x == self.head.data:
                self.head = None 
            else:
                print("x is not in DLL")
                return 
        # delete first Node
        if self.head.data == x:
            self.head = self.head.next 
            self.head.prev = None 
            return 
        # middle node delete
        n = self.head 
        while n.next is not None:
            if x == n.data:
                break 
            n = n.next 
        if n.next is not None:
            n.next.prev = n.prev
            n.prev.next = n.next 
        else:
            # delete last node
            if n.data == x:
                n.prev.next = None 
            else: 
                print("x is not in dll")

    def circular_doubly_make_circle(self):
        if self.head is None:
            return 
        n = self.head 
        while n.next is not None:
            n = n.next 
        n.next = self.head 
        self.head.prev = n

    def circular_doubly_traverse(self):
        if self.head is None:
            return 

        n = self.head
        while True:
            n = n.next
            if n == self.head:
                print('doubly circular')
                break


dll = DLinkedList()
dll.empty_node(40)
dll.add(30)
dll.add(20)
dll.add(10)
#dll.print_LL()
#dll.print_reverse()
dll.add_end(50)
dll.print_LL()
dll.add_at_index(35, 30)
dll.print_LL()
dll.delete_at_begin()
dll.print_LL()
dll.delete_at_end()
dll.print_LL()
dll.circular_doubly_make_circle()
dll.circular_doubly_traverse()