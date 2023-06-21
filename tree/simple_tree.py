class node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def print(self):
        self._print(self)
        
    def _print(self, root):
        if root is None:
            return
        print(root.value)
        self._print(root.left)
        self._print(root.right)

root = node(5)
root.left = node(10)
root.right = node(20)
root.left.left = node(40)
root.print()

#5
#10
#40
#20
