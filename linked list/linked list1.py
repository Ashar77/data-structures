class ListNode:
    def __init__(self,value):
        self.data = value
        self.next = None
    
    def traverse(self):
        a = self
        while a is not None:
            print(a.data)
            a = a.next

    def insert(self,after,data):
        new = ListNode(data)
        after.next = new
        


a = ListNode(17) 
#print(a.data)
#print(a.next)

# a.next = ListNode(5)
# print(a.next)
# print(a.next.data)
# print(a.next.next)

# a.next.next = ListNode(5)
# print(a.next.next)
# print(a.next.next.data)
# print(a.next.next.next)  #none

b = ListNode(4)
a.next = b 
# print(a.next)
# print(b) 
# print(b.data)
# print(a.next.data)


#a.traverse()
print('a is',a)

c = ListNode(3)
b.next = c

a.traverse()





