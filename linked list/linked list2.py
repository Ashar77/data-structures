
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.start = None
   
    def insertLast(self,value):
        newNode = Node(value)
        if self.start == None:
            self.start = newNode
        else:
            temp = self.start
            while temp.next!=None:
                temp = temp.next
            temp.next = newNode

    def deleteFirst(self):
        if self.start == None:
            print('linked list is empty!')
        else:
            self.start = self.start.next

    # def insertFirst(self,value):
    #     newNode =  Node(value)
    #     newNode.data = self.start
    #     self.start = newNode



    def deleteLast(self):
        temp2 = self.start
        while temp2.next != None:
            temp2 = temp2.next
        temp2.data = None

    def viewList(self):
        if self.start == Node:
            print('list is empty')
        else:
            temp3 = self.start
            while temp3!=None:
                print(temp3.data)
                temp3=temp3.next


myList = LinkedList()
myList.insertLast(6)
myList.insertLast(88)
myList.viewList()
myList.deleteFirst()
print('sssss')
myList.viewList()
print('--------------')
myList.insertLast(7777)
myList.insertLast(6675)
myList.viewList()
myList.deleteLast()
myList.deleteLast()