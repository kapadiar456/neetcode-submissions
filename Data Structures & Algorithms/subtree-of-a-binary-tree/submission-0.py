# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs(root, res):
            if root == None:
                res.append("null")
                return
            res.append(str(root.val))
            dfs(root.left, res)
            dfs(root.right, res)
            return res
        treeList =dfs(root, [])
        subtreeList = dfs(subRoot, [])
        quote = ''
        tree = quote.join(treeList)
        sub = quote.join(subtreeList)
        if sub in tree:
            return True
        else:
            return False

        

        
        
