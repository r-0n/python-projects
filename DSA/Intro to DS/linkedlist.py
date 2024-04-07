class Node:

    data = None
    next_node =None

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return "<Node data: %s>"% self.data
    

class linked_list:
    """Singly LinkedList"""

    def __init__(self):
        self.head=None

    def is_empty(self):
        return self.head==None
    
    def size(self):
        """Returns the number of nodes in the
        LinkedList. takes O(n) time"""
        
        current = self.head
        count =0

        while current !=None:
            count+=1
            current = current.next_node
        
        return count

    def add(self, data):
        """
        Adds a new node containing data 
        at the head of the list takes O(1)
        """
        new_node = Node(data)
        new_node.next_node = self.head
        self.head= new_node


    
    def search(self, key):

        """Search for the first node whose data 
        matches the key
        returns None if key isn't found
        rans in O(n) time"""

        current = self.head

        while current:
            if current.data == key:
                return current
            else: 
                current = current.next_node
        return None

    def insert(self, data, index):
        """Inserts data at a specific index
        runs in O(1) time for inserting
        finding the index takes O(n) time
        overall time complexity: O(n)
        """
        if index ==0:
            self.add(data)

        if index>0:
            new =Node(data) 
            position = index
            current = self.head

            while position>1:
                current = Node.next_node
                position-=1

            prev_node = current
            next_node = current.next_node

            prev_node.next_node =new
            new.next_node = next_node


    def remove(self, key):
        """removes a node from the linkedlist that matches the key
        returns the key if it doesn't exist
        
        runs in O(n) time"""
        current = self.head
        previous = None
        found = False

        while current and not found:
            if current.data == key and current is self.head:
                found =True
                self.head = current.next_node

            elif current.data ==key:
                found=True
                previous.next_node =current.next_node

            else:
                previous =current
                current = current.next_node

        return current
    

    #def sort_linkedlist(self)



    def __repr__(self):
        """Returns a string representation of the list 
        takes O(n) time"""

        nodes = []
        current = self.head

        while current:
            if current is self.head:
                nodes.append("[Head: %s]" %current.data)
            elif current.next_node is None:
                nodes.append("[Tail: %s]" % current.data)
            else: 
                nodes.append("[%s]" % current.data)

            current = current.next_node
        return '->'.join(nodes)
    


l = linked_list()
l.add(10)
l.add(45)
l.add(1010)
n= l.search(10)
print(l)
print(n)


