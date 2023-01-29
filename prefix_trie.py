
class Node:
    def __init__(self):
        self.children = {}
        self.isWord = False

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        temp = self.root
        for a in word:
            if a not in temp.children:
                temp.children[a] = Node()
            temp = temp.children[a]
        temp.isWord = True

    def search(self, word):
        temp = self.root
        for a in word:
            if a not in temp.children:
                return False
            temp = temp.children[a]
        return temp.isWord == True

    def startsWith(self, word):
        temp = self.root
        for a in word:
            if a not in temp.children:
                return False
            temp = temp.children[a]
        return True



ob1 = Trie()
ob1.insert("apple")
print(ob1.search("apple"))
print(ob1.search("app"))
print(ob1.startsWith("app"))
ob1.insert("app")
print(ob1.search("app"))

#True
#False
#True
#True
