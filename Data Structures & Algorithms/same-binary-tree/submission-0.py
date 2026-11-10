# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(node, res):
            if node == None:
                res.append('placeholder')
                return
            else:
                res.append(node.val)
            dfs(node.left, res)
            dfs(node.right, res)
            return res
        res1 = dfs(p,[])
        res2 = dfs(q, [])
        return res1==res2
