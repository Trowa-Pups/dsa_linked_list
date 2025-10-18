class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head:
            new_node.next = self.head
            self.head = new_node

        else:
            self.tail = new_node
            self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head:
            self.tail.next = new_node
            self.tail = new_node
            
        else:
            self.head = new_node
            self.tail = new_node

    def search (self, data):
        current_node = self.head
        while current_node:
            if current_node.data == data:
                return True
    
            else:
                current_node = current_node.next
        
        return False
    
    def remove_beginning(self):
        if not self.head:  #Checks if node is empty
            return None
        removed_data = self.head.data  #Saves the old head’s data
        self.head = self.head.next  #The next node turns into the new head
        if not self.head:  # hecks if the list became empty
            self.tail = None  
        return removed_data  
    
    def remove_at_end(self):
        if not self.head: #Checks if node is empty
            return None
        if self.head == self.tail: #Checks if there is only one element
            removed_data = self.head.data #Saves the data of the node
            self.head = None
            self.tail = None
            return removed_data

        current = self.head #Starts from the head
        while current.next != self.tail: #Loops until finding the second node
            current = current.next 
        removed_data = self.tail.data
        current.next = None
        self.tail = current #Updates tail to the new last node
        return removed_data

    def remove_at(self, data):
        if not self.head:  #Checks if the list is empty
            return None
        if self.head.data == data:  #Checks if the head is the one to remove
            return self.remove_beginning()

        current = self.head  #Starts from the head
        while current:  #Loops through each node
            if current.next and current.next.data == data:  #Checks the next node’s data
                removed_data = current.next.data  #Saves the data to be removed
                current.next = current.next.next
                if current.next is None: 
                    self.tail = current  #Updates the tail           
                return removed_data 
            current = current.next  #Moves to the next node

        return None


sushi_preparation = LinkedList()
sushi_preparation.insert_at_end("prepare")
sushi_preparation.insert_at_end("roll")
sushi_preparation.insert_at_beginning("assemble")

print(f"Search: {sushi_preparation.search('roll')}, {sushi_preparation.search('mixing')}") #Search
print(f"Removed Beginning: {sushi_preparation.remove_beginning()}") #Returns the removed beginning node
print(f"Removed End: {sushi_preparation.remove_at_end()}") #Returns the removed end node
print(f"Removed Specific: {sushi_preparation.remove_at('prepare')}") #Returns the removed specified node 
