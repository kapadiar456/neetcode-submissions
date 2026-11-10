# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(root):
            if root == None:
                return
            left = dfs(root.left)
            res.append(1)
            if len(res) == k:
                return root.val
            right = dfs(root.right)
            if left is not None:
                return left
            else:
                return right
        res = []
        return dfs(root)
