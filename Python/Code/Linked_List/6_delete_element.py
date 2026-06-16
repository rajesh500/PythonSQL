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
                curr = curr.next 
            node.next = curr.next 
            curr.next = node 
            return node

    def delete(self, data):
        if self.head is None:
            return None
        else:
            self.head = self.head.next
        
    def delete_end(self, value):
        if self.head is None:
            return None
        else:
            curr = self.head
            while curr.next.next is not None:
                curr = curr.next
            curr.next = None
        
    def delete_at_index(self, value):
        if self.head is None:
            return None
        curr = self.head

        while curr.next is not None:
            if curr.next.data == value:
                curr.next = curr.next.next
                return
            curr = curr.next
                
        # for i in range(1, pos):
        #     #print(curr.data, 'delete at index')
        #     curr= curr.next
        # curr.next = curr.next.next
        
    def traverse_sli(self):
        if self.head is None:
            return self.head
        n = self.head 
        while n.next is not None:
            print(n.data)
            n =  n.next
        print(n.data)

    def traverse_backward(self):
        if self.head is None:
            return self.head 
        
        prev_node = None
        current_node = self.head

        while current_node is not None:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
            #(prev_node.data, end = "<->")
        self.head = prev_node
        return self.head
    
        #print(prev_node)
    def traverse_back_print(self):
        cur = self.head
        while cur is not None:
            print(cur.data, end=" -> ")
            cur = cur.next
        print()

LL = LinkedList()
LL.add(1)
LL.add(2)
LL.add(3)
LL.add(4)
LL.add(5)
# LL.add_at_index(40,2)
# LL.add_at_index(45,3)
# LL.add(50)
# LL.add_at_index(5,0)
# LL.delete(15)
# #LL.print_LL()
# LL.delete_end(50)
# #LL.print_LL()
# LL.delete_at_index(45)
# print(LL)
# LL.print_LL()
res = LL.traverse_backward()
LL.traverse_back_print()
# LL.print_LL()