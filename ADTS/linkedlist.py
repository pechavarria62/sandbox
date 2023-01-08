# MODIFY ME TO IMPLEMENT YOUR SOLUTION
# TO PROBLEM 1: Linked List
#
# NAME:         Pedro Echavarria
# ASSIGNMENT:   Project 5: Implementing ADTs

from Node import Node

class LinkedList(object):
    def __init__(self, list=None):
        self.head = None
        if list is not None:
            for item in list:
                self.add(item)

    # Returns the data in the head node, and None otherwise.
    def get_head(self):
        return self.head.get_data() # type: ignore

    # Inserts a new Node with data into the front of the list.
    def add(self, data):
        # if head (top) is empty insert the new Node with the data.
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            return
        current_node =  self.head
        self.head = new_node
        self.head.set_next(current_node)

    # Returns True if data is in the list, or False     
    def search(self, data):
        if self.is_empty(): 
            return False
        else: # if not insert the heat to current_node
            current_node =  self.head
            # Traverse/iterate through the data set and return true if you find the data and false other wise.
            while current_node != None:
                if data == current_node.get_data():
                    return True
                else:
                    current_node = current_node.get_next()
        return False

    # Traverse/iterate through the data set and return data if found and removes it, otherwise returns None
    def delete(self, data):
        if self.is_empty(): # if node is empty return false.
            return None
        else: # if not insert the heat to current_node
            previous_node = None
            current_node =  self.head
            while current_node != None: # Traverse the data set & get data if found.
                if data == current_node.get_data(): 
                    if current_node == self.head:
                        self.head = current_node.get_next()
                    else:
                        previous_node.set_next(current_node.get_next()) # type: ignore
                        
                    return current_node.get_data()
                else:
                    previous_node = current_node
                    current_node = current_node.get_next()
        return None
    # Display the Stack.
    def print(self):
        n = self.head
        while n is not None:
            print(n.get_data(), "=>", end=" ")
            n = n.get_next()
        print("NULL")

    # Return True if the list is empty, or False otherwise.
    def is_empty(self):
        if self.head == None:
            return True
        return False

    # Empty the list
    def clear(self):
        self.head = None
        return

def main():
    l = list(range(1, 5))
    l.reverse()
    ll = LinkedList(l)
    ll.print()
    print("Search 4: ", ll.search(4))
    print("Search 5: ", ll.search(5))
    print("Delete 5: ", ll.delete(5))
    print("Delete 4: ", ll.delete(4))
    ll.print()
    print("Delete 1: ", ll.delete(1))
    ll.print()

# Don't run main on import
if __name__ == "__main__":
    main()

