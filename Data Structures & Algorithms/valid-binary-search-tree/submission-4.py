# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, minimum, maximum):
            left = False
            right = False
            if root == None:
                return True
            if minimum < root.val < maximum:
                left = dfs(root.left, minimum, root.val)
                right = dfs(root.right, root.val, maximum)
            else:
                return False
            if left == True and right == True:
                return True
            else:
                return False
        
        return dfs(root, float("-inf"), float("inf"))