class stack:
    def __init__(self,max):
        self.max = max
        self.stack = []

    def push(self,element):
        if len(self.stack)==self.max:
            print("overflow")
        self.stack.append(element)

    def pop(self):
        if len(self.stack)==0:
            print('overflow')
        self.stack.pop()

    def index_pop(self,index):
        self.index = index
        if self.stack[self.index]:
            self.stack.pop(index)

    def isEmpty(self):
        if len(self.stack)==0:
            return True
        else:
            return False
    def traverse(self):
        if len(self.stack)==0:
            print('stack is empty')
        else:
            for i in self.stack:
                print(i)




