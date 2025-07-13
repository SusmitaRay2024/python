class Node:
    def __init__(self, prev = None, item = None, next = None):
        self.prev = prev
        self.item = item
        self.next = next
        
class CDLL:
    def __init__(self, start = None):
        self.start = start
    
    def is_empty(self):
        return self.start == None
    
    def insert_at_start(self, data):
        n = Node(item=data)
        if self.is_empty():
            n.next = n
            n.prev = n 
        else:
            n.next = self.start
            n.prev = self.start.prev
            self.start.prev.next = n
            self.start.prev = n
        self.start = n 
        
    def insert_at_last(self,data):
        n = Node(item= data)
        if self.is_empty():
            n.next = n
            n.prev = n 
            self.start = n 
        else: 
            n.next = self.start
            n.prev = self.start.prev
            self.start.prev.next = n
            self.start.prev = n
            
    def search(self, data):
        temp = self.start
        if temp == None:
            return None
        if temp.item == data:
            return temp
        else:
            temp = temp.next
            while temp != self.start:
                if temp.item == data:
                    return temp
                temp = temp.next
            return None 
        
    def insert_after(self, temp, data):
        if temp != None:
            n = Node(item = data)
            n.next = temp.next
            n.prev = temp
            temp.next.prev = n
            temp.next = n
    
    def print_list(self):
        temp = self.start
        if temp != None:
            print(temp.item, end=" ")
            temp= temp.next
            while temp != self.start:
                print(temp.item, end=" ")
                temp = temp.next
    
    def delete_at_first(self):
        if self.start is not None:
            if self.start.next == self.start: # expected 2 nodes in the list 
                self.start = None
            else: 
                self.start.prev.next = self.start.next
                self.start.next.prev = self.start.prev
                self.start = self.start.next
                
    def delete_at_last(self):
        if self.start is not None:
            if self.start.next == self.start: 
                self.start = None
            else: 
                self.start.prev.prev.next = self.start
                self.start.prev = self.start.prev.prev
                
    def delete_item(self, data):
        temp = self.start
        if temp.item == data:
            self.delete_at_first()
        else: 
            temp = temp.next
            while temp != self.start:
                if temp.item == data: 
                    temp.next.prev = temp.prev
                    temp.prev.next = temp.next 
                    
mylist = CDLL()
mylist.insert_at_start(10)
mylist.insert_at_last(20)
mylist.insert_at_last(30)
mylist.insert_at_last(40)
mylist.print_list()
print()
# mylist.insert_after(mylist.search(30), 35)



    