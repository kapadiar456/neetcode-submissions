class Node:
    def __init__(self, val_, key_):
        self.val = val_
        self.key = key_
        self.right = None
        self.left = None
class TreeMap:
    
    def __init__(self):
        self.root = None
        

    def insert(self, key: int, val: int) -> None:
        def dfs(node, key):
            if node== None:
                return Node(val, key)
            if node.key>key:
                node.left = dfs(node.left, key)
            elif node.key<key:
                node.right = dfs(node.right, key)
            return node

        if self.root==None:
            self.root = Node(val, key)
        else:
            dfs(self.root, key)
            
    def get(self, key: int) -> int:
        def dfs(node, key):
            if node == None:
                return -1
            elif node.key==key:
                return node.val
            elif node.key>key:
                return dfs(node.right, key)
            elif node.key<key:
                return dfs(node.right, key)
        return dfs(self.root, key)

    def getMin(self) -> int:
        if self.root == None:
            return -1
        while self.root and self.root.left:
            self.root=self.root.left
        return self.root.val


    def getMax(self) -> int:
        if self.root == None:
            return -1
        while self.root and self.root.right:
            self.root=self.root.right
        return self.root.val

    def remove(self, key: int) -> None:
        def getMaxVal(root):
            while self.root and self.root.right:
                self.root=self.root.right
            x = self.root.key
            y = self.root.val
            return (x,y)

        def dfs(root, key):
            if root==None:
                return
            elif root.key>key:
                root.left = dfs(root.left,key)
            elif root.key<key:
                root.right = dfs(root.right, key)
            elif root.key==key:
                if not root.left:
                    return root.right
                elif not root.right:
                    return root.left
                else:
                    x,y = getMaxVal(root)
                    root.key = x
                    root.val = y
                    root.right = dfs(root.right, root.key)
            return root
        self.root = dfs(self.root, key)
                

    def getInorderKeys(self) -> List[int]:
        res= [] 
        def dfs(root):
            if root==None:
                return
            dfs(root.left)
            res.append(root.key)
            dfs(root.right)
        dfs(self.root)
        return res
