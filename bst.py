class bst():
    def __init__(self, data):
        self.data=data
        self.left=None
        self.right=None

    def add(self, data):
        if data <= self.data:
            if self.left is None:
                self.left=bst(data)
            else:
                self.left.add(data)
        else:
            if self.right is None:
                self.right=bst(data)
            else:
                self.right.add(data)

    def inorder(self):
        if self is None:
            return
        if self.left is not None:
            self.left.inorder()
        print(self.data, end=' ')
        if self.right is not None:
            self.right.inorder()


a=bst(7)
for i in [15, 10, 2, 12, 3, 1, 13, 6, 11, 4, 14, 9]:
    a.add(i)
a.inorder()
