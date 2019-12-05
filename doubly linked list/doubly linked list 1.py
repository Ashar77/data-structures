class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def append(self,data):
        if self.head == None:  # when there is no element in list 
            new_Node = Node(data)
            self.head = new_Node
            new_Node.prev = None

        else:
            new_Node = Node(data) # when there is already atleast one element
            cur_node = self.head
            while cur_node.next != None:
                cur_node = cur_node.next
            cur_node.next = new_Node
            new_Node.prev = cur_node
            new_Node.next = None

    def prepend(self,data):
        if self.head == None:  # when there is no element in list 
            new_Node = Node(data)
            self.head = new_Node
            new_Node.prev = None
        
        else:
            new_Node = Node(data)
            new_Node.prev = None
            new_Node.next = self.head
            self.head = new_Node
            self.head.prev = new_Node


    def add_after_node(self, key, data):
        cur = self.head
        while cur != None:
            if cur.next is None and cur.data == key: # if there is only one node 
                self.append(data)
                return
            
            elif cur.data == key:
                new_Node = Node(data)
                nxt = cur.next
                cur.next = new_Node
                new_Node.next = nxt
                new_Node.prev = cur
                nxt.prev = new_Node
            cur = cur.next 

    def add_before_node(self,key,data):
        cur = self.head
        while cur!=None:
            if cur.prev is None and cur.data == key:
                self.prepend(data)
                return
            
            elif cur.data == key:
                new_Node = Node(data)
                new_Node.next = cur
                cur.prev = new_Node
                bef = cur.prev
                bef.next = new_Node
                new_Node.prev = bef   
        cur = cur.next

    def delete(self,key):
        cur = self.head
        while cur is not None:
            if cur.data == key and cur==self.head:
                    #case1 # ONLY ONE NODE IN THE LIST 
                if cur.next is None:
                    cur = None
                    self.head = None
                    return
                    #case 2 we want to remove the head node and there are more then one node in the list
                
                else:
                    nxt = cur.next
                    cur.next = None
                    nxt.prev = None
                    cur = None
                    self.head = nxt
                    return
                  
            elif cur.data == key:
            
                    # case3 when the node is in between
                
                if cur.next is not None:
                    nxt = cur.next
                    prev = cur.prev
                    prev.next = nxt
                    nxt.prev = prev
                    cur.next = None
                    cur.prev = None
                    cur = None
                    return
            else: #deleting the last node 
                    prev = cur.prev
                    prev.next = None
                    cur.prev = None
                    cur = None
                    return
            cur = cur.next

    def print_list(self):
        cur = self.head
        while cur!=None:
            print(cur.data)
            cur = cur.next



D = DoublyLinkedList()
D.append(1)
D.append(2)
D.append(3)
# D.prepend(0) 
# # D.prepend(5)
# D.add_after_node(1,7)
# D.add_after_node(2,12)
# D.add_after_node(3,99)
# D.print_list()



#D.add_before_node(2,24)
D.print_list()
D.delete(3)
print()
D.print_list()