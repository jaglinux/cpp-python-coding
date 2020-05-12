class node():
    def __init__(self, data):
        self.data=data
        self.next=None

class ll():
    def __init__(self):
        self.root=None

    def add(self, data):
        a=node(data)
        if self.root is None:
            self.root=a
        else:
            temp=self.root
            while temp:
                if temp.next is None:
                    temp.next=a
                    return
                else:
                    temp=temp.next

    def print(self):
        print('Link List is')
        temp=self.root
        while temp:
            print(temp.data)
            temp=temp.next

def reverse_rec(temp, prev):
    if temp.next is None:
        temp.next=prev
        return temp
    else:
        head=reverse_rec(temp.next, temp)
        temp.next.next=temp
        temp.next.next.next=None
        return head

def reverse(head):
    if head is None:
        return None
    return reverse_rec(head, None)

a=ll()
for i in range(3):
    a.add(i)
a.print()
a.root=reverse(a.root)
a.print()

'''
Link List is
0
1
2
Link List is
2
1
0
'''
