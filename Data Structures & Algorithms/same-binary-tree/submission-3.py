# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(p, q):
            if p == None and q == None:
                return True
            if q == None:
                return False
            if p == None:
                return False
            if p.val != q.val:
                return False
            left = dfs(p.left, q.left)
            right = dfs(p.right, q.right)
            if left == False or right == False:
                return False
            else:
                return True
        return dfs(p,q)

            
            