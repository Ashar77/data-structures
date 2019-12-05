class Stack:
    def __init__(self):
        self.items = []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def get_stack(self):
            return self.items

    def isEmpty(self):
        return self.items == []



s = Stack()
s.push('a')
s.push('b')
s.push('c')
print(s.get_stack())
print(s.isEmpty())
    