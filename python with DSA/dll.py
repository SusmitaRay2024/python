class Node:
    def __init__(self, prev=None, item=None, next=None):
        self.prev = prev
        self.item = item
        self.next = next

class DLL:
    def __init__(self, start):
        self.start = start
    
    def is_empty(self):
        return self.start == None
    
    def insert_at_start(self, data):
        n = Node(None, data, self.start)
        if not self.is_empty():
            self.start.prev = n
        self.start = n
        
    def insert_at_last(self, data):
        temp = self.start
        if self.start is not None: #not empty
            while temp.next != None: #traversing
                temp = temp.next
                
        n = Node(temp, data, None)
        if temp == None:     #if list was empty
            self.start = n
        else: 
            temp.next = n
            
    def search(self, data):
        temp = self.start
        while temp != None:
            if temp.item == data:
                return temp #found the node
            temp = temp.next
        return None #Not found
    def insert_after(self, temp, data):
        if temp != None:
            n = Node(temp, data, temp.next)
            if temp.next is not None:
                temp.next.prev = n
            temp.next = n
            
    def print_list(self):
        temp = self.start
        while temp is not None:
            print(temp.item, end=" ")
            temp = temp.next
            
    def delete_first(self):
        if self.start is not None:
            self.start = self.start.next
            if self.start is not None:
                self.start.prev = None
                
    def delete_last(self):
        if self.start == None:
            pass #list already empty
        elif self.start.next is None:
            self.start = None #Only one node
        else: 
            temp = self.start
            while temp.next is not None:
                temp = temp.next #identify last node
            temp.prev.next = None
                
    def delete_item(self,data):
        if self.start == None:
            pass
        else:
            temp =self.start
            while temp is not None:
                if temp.item == data:
                    if temp.next is not None:
                        temp.next.prev = temp.prev #Link next node back to previous node
                    if temp.prev is not None:
                        temp.prev.next= temp.next #link previous node to next node
                    else:
                        self.start = temp.next  #first node, move start
                    break
                temp =temp.next
            return None
            
            
                