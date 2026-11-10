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


    def dfs(self, word, ptr):
        if ptr.end == True and word == '':
            return True
        if ptr.end == False and word == '':
            return False
        c = word[0]
        if c in ptr.children:
            return self.dfs(word[1:], ptr.children[c])
        elif c == '.':
            for k, v in ptr.children.items():
                if self.dfs(word[1:], v):
                    return True
            return False
        else:
            return False


    def search(self, word: str) -> bool:
        return self.dfs(word, self.root)