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
                print(n.data, end= '-->')
                n = n.next 
            print()

    def add(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = newNode

    def make_circle(self):
        if self.head is None:
            return 
        n = self.head 
        while n.next is not None:
            #print(n.data)
            n = n.next
        n.next = self.head

    def circular_singly_ll_traverse(self):
        if self.head is None:
            return 
        
        n = self.head
        while True:
            print(n.data)
            n = n.next
            if n == self.head:
                print('circular')
                break
        
    def csll_add_begin(self, data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
            newnode.next = self.head 
        n = self.head 
        newnode.next = self.head
        self.head = newnode

    def csll_add_at_index(self, x, data):
        newNode = Node(data)
        if self.head is None:
            return 
        n = self.head
        while n is not None:
            #print(n.data, 'at index')
            if n.data == x:
                print("found x")
                break
            n = n.next
        newNode.next = n.next
        n.next = newNode
            
    def csll_delete(self):
        if self.head is None:
            return 
        self.head = self.head.next
    
    def csll_delete_end():pass  # check singly linked list delete
    def csll_delete_at_index():pass # check singly linked list delete
        
    

LL = LinkedList()
LL.add(1)
LL.add(2)
LL.add(3)
LL.add(4)
LL.add(5)                            
LL.print_LL()
LL.csll_add_begin(0)
LL.print_LL()
#LL.make_circle()
#LL.circular_singly_ll_traverse()
LL.csll_add_at_index(3, 3.5)
LL.print_LL()
# LL.make_circle()
# LL.circular_singly_ll_traverse()
LL.csll_delete()
LL.print_LL()