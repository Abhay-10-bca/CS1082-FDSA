class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None  

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    
    def append_node(self, data):
        new_node = Node(data) 
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next: 
                current = current.next
            current.next = new_node 
   
    def search_node(self, data):
        current = self.head
        while current:  
            if current.data == data:
                return True  
            current = current.next
        return False  

    
    def display_list(self):
        current = self.head
        if not current:
            print("The list is empty.")
            return
        while current:
            print(current.data, end=" -> " if current.next else "")
            current = current.next
        print()  


if __name__ == "__main__":
    linked_list = SinglyLinkedList()
    
    
    linked_list.append_node(10)
    linked_list.append_node(20)
    linked_list.append_node(30)
    
    
    print("Linked List:")
    linked_list.display_list()

    
    print("Is 20 in the list?", linked_list.search_node(20))  
    print("Is 40 in the list?", linked_list.search_node(40))  
