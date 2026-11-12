class TrieNode:
    def __init__(self, word):
        self.children = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode(False)

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode(False)
            curr = curr.children[c]
        curr.word = True

    def search(self, word: str) -> bool:
        curr = self.root
        for index in range(len(word)):
            if word[index] == '.':
                boolarr = []
                for k,v in curr.children.items():
                    if k not in curr.children:
                        continue
                    curr = curr.children[k]
                    if self.search(word[index+1:]) ==True:
                        return True
            if word[index] not in curr.children:
                return False
            curr = curr.children[word[index]]
        return True
