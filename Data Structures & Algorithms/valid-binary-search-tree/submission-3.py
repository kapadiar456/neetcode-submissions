# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if root == None:
                return True
            if (root.right == None or root.right.val > root.val) and (root.left == None or root.left.val < root.val):
                left = dfs(root.right)
                right = dfs(root.left)
            else:
                return False
            if left == True and right == True:
                return True
            else:
                return False
        return dfs(root)