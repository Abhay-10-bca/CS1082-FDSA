class CircularNode:
    def __init__(self, data):
        self.node = data
        self.next = None
    
class CircularLinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_beginning(self, data):
        new_node = CircularNode(data)
        
        if self.head == None:
            new_node.next = new_node
            self.head = new_node
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            
            temp.next = new_node
            new_node.next = self.head
            self.head = new_node
            
    def delete_node(self):
        if self.head is None:
            print("Empty List")
            return

       
        if self.head.next == self.head:
            self.head = None
            return
        
        
        temp = self.head
        while temp.next != self.head:
            temp = temp.next

       
        self.head = self.head.next
        temp.next = self.head
        
    def display(self):
        if self.head is None:
            print("The list is empty!")
            return
        
        temp = self.head
        while True:
            print(temp.node, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print("(head)")    
    
    
circular=CircularLinkedList()
circular.insert_at_beginning(5)
circular.insert_at_beginning(7)
circular.insert_at_beginning(9)
circular.insert_at_beginning(11)
circular.display()


circular.delete_node()
circular.display()

    

    
    
