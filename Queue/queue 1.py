# front and rear should be -1 if the queue is empty
class myqueue:
    def __init__(self):
        self.q = list()

    def __len__(self):
        return len(self)

    def isEmpty(self):
        return len(self.q)==0

    def enqueue(self,item):
        self.q.append(item)  # add in the last

    def dequeue(self):
        return self.q.pop(0)  # removing from the front

    def traverse(self):
        for i in range(len(self.q)):
            print(self.q[i],end=" ")


q1 = myqueue()
#print(q1.isEmpty())
q1.enqueue('a')
q1.enqueue('b')
q1.enqueue('c')
q1.traverse()
q1.dequeue()
print()
q1.traverse()
print(q1.isEmpty())
print(len(q1))