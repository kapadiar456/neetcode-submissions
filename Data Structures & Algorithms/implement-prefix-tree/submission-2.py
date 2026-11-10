class Node:
    def __init__(self, value):
        self.val = value
        self.children = {}
        self.end = False
        
class PrefixTree:

    def __init__(self):
        self.root = Node(-1)
        

    def insert(self, word: str) -> None:
        ptr = self.root
        newNode = None
        for c in word:
            if c not in ptr.children:
                newNode = Node(c)
                ptr.children[c] = newNode
                ptr = newNode
            else:
                newNode = ptr.children[c]
                ptr = newNode
        if newNode:
            newNode.end = True

    def search(self, word: str) -> bool:
        ptr = self.root
        newNode = None
        for c in word:
            if c not in ptr.children:
                return False
            ptr = ptr.children[c]

        if ptr.end == True:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        ptr = self.root
        newNode = None
        for c in prefix:
            if c not in ptr.children:
                return False
            ptr = ptr.children[c]
        return True
        