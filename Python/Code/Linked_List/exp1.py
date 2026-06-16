class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


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


LL = Node()
LL.add(15)
LL.add(10)
LL.print_LL()