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


    
