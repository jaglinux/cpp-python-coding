class node():
    def __init__(self, data):
        self.data= data
        self.next=None

class circular():
    def __init__(self):
        self.root=None

    def add(self, data):
        a=node(data)
        if self.root is None:
            self.root=a
            a.next=self.root
        else:
            a.next=self.root.next
            self.root.next=a

    def print(self):
        if self.root is None:
            return
        print(self.root.data)
        temp=self.root
        while temp.next is not self.root:
            temp=temp.next
            print(temp.data)
c=circular()
for i in [5,7,3,8,9]:
    c.add(i)
c.print()
