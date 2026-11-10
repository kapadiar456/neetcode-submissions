# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, minVal, maxVal):
            if root == None:
                return True
            if minVal < root.val < maxVal:
                right = dfs(root.right, root.val, maxVal)
                left = dfs(root.left, minVal, root.val)
                if left == True and right == True:
                    return True
                else:
                    return False
            else:
                return False
        return dfs(root, float("-inf"), float("inf"))