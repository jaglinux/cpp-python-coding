class Q():
    def __init__(self):
        self.list=[]

    def push(self, data):
        self.list.insert(0,data)

    def pop(self):
        if len(self.list):
            return self.list.pop()

    def top(self):
        if len(self.list):
            return self.list[-1]

a=Q()
print(a.pop())
print(a.top())
a.push(1)
a.push(2)
a.push(3)
print(a.top())
print(a.pop())
a.push(1)
print(a.top())

