class Node:
    def __init__(self, val):
        self.val = val
        self.end = False
        self.children = {}

class WordDictionary:

    def __init__(self):
        self.root = Node(-1)

    def addWord(self, word: str) -> None:
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
        for c in word:
            if c not in ptr.children and c != '.':
                return False
            else:
                if c == '.':
                    if ptr.children:
                        for k, v in ptr.children.items():
                            ptr = v
                else:
                    ptr = ptr.children[c]
        return True
        
