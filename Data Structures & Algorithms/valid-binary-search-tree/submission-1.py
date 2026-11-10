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
            if root.val > minVal and root.val<maxVal:
                ans1 = dfs(root.left, minVal, root.val)
                ans2 = dfs(root.right, root.val, maxVal)
                if ans1 == True and ans2 == True:
                    return True
                else:
                    return False
            else:
                return False
        return dfs(root, -float('inf'), float('inf'))
