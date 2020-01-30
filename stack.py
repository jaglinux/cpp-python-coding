class Stack():
    def __init__(self):
        self.list=[]

    def push(self, data):
        self.list.append(data)

    def pop(self):
        if len(self.list):
            return self.list.pop()
        return None

    def top(self):
        if len(self.list):
            return self.list[-1]
        return None

a=Stack()
print(a.top())
print(a.pop())
a.push(3)
a.push(2)
a.push(5)
print(a.top())
print(a.pop())
print(a.top())
