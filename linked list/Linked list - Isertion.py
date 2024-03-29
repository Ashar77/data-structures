class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None


    def printList(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next



    def append(self,data):
        new_node = Node(data)

        if self.head == None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next != None:
            last_node = last_node.next
        last_node.next = new_node


    def prepend(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self,prev_node,data):

        if not prev_node:
            print('previous node is not in the list')
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

        

L = LinkedList()
L.append('A')
L.append('B')
L.append('C')
L.append('D')

#L.prepend('E')

L.insert_after_node(L.head.next,'E')
L.printList()
