class node():
    def __init__(self, data):
        self.data=data
        self.prev=None
        self.next=None

class double():
    def __init__(self):
        self.root=None
        self.tail=None

    def add(self, data):
        a=node(data)
        if self.root is None:
            self.root = a
            self.tail = a
        else:
            self.root.prev=a
            a.next=self.root
            self.root=a

    def print(self):
        print('print next')
        temp=self.root
        while temp is not None:
            print(temp.data)
            temp=temp.next

    def print_tail(self):
        print('print prev')
        temp=self.tail
        while temp is not None:
            print(temp.data)
            temp=temp.prev

d=double()
for i in [5, 9, 3, 8]:
    d.add(i)
d.print()
d.print_tail()
