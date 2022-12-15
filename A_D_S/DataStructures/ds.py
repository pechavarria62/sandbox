
# print ("arrays")


# list = [1,2,3]
# result = list[0]

# if 1 in list: print(True)

# for n in list:
#     if n == 1:
#         print(True)

#         break
# print("***************************************************")
# print("Linked list")

class Node:
    '''

    An object for storing a single node of a linked list.
    Models two attributes - data and the link to the node  in the list. 

    '''
    data = None
    next_node = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return "<Node data: %s>" % self.data

class linkedList: #sigly linked list.
    
    '''
    Singly linked list.

    '''

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None
    
    def size(self):
        '''
        Returns the number of nodes in the list
        Takes 0(n) time
        '''
        current = self.head
        count = 0

        while current:
            count += 1
            current = current.next_node

        return count
    def add(self, data):
        '''
        Adds new node containing data at head of the list
        Take 0(1) time
        '''
        new_node = Node(data)
        new_node.next_node = self.head 
        self.head = new_node
    
    def search(self, key):
        '''
        Search for the first node containing data that matches the key.
        Return the node or 'None' if not found.
        Takes 0(n) time.
        '''
        current = self.head

        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node
        return None

    def insert(self, data, index):
        '''
        Inserts a new Node containing data at index position
        Inserts takes 0(1)= constant time but finding at the insertion point takes 0(n)= linear time.

        Takes overall 0(n) time
        '''

        if index < 0: 
            self.add(data) 
        
        if index > 0: 
            new = Node(data) 

            position = index 
            current = self.head 

            while position > 1:
                current = Node.next_node
                position -= 1
            
            prev_node = current
            next_node = current.next_node #type: ignore
            prev_node.next_node = new #type: ignore
            new.next_node = next_node

    def remove(self, key):
        '''
        Removes Node containing data that matches the key.
        Returns the Node or None if key doesn't exist.
        Take 0(n) time
        '''
        current = self.head
        previous = None
        found = False


        while current and not found:
            if current.data is key and current is self.head:
                found = True
                self.head = current.next_node
            elif current.data == key:
                found = True
                previous.next_node = current.next_node #type: ignore
            else:
                previous = current
                current = current.next_node

    def node_at_index(self, index):
        if index == 0 :
            return self.head
        else:
            current = self.head
            position = 0

            while position < index:
                current = current.next_node #type: ignore
                position += 1

            return current

    def __repr__(self):
        '''
        Return a string representation of the list
        Takes 0(n) time
        '''
        nodes = []
        current = self.head

        while current:
            if current is self.head:
                nodes.append("[Head: %s]" % current.data)
            elif current.next_node is None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)

            current = current.next_node
        return ' -> '.join(nodes)
        