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
            if root.right and root.left:
                if root.val < root.right.val and root.val > root.left.val:
                    val1 = dfs(root.left)
                    val2 = dfs(root.right)
                    if val1 == True and val2 == True:
                        return True
                    else:
                        return False
            elif root.right and not root.left:
                if root.right.val> root.val:
                    return dfs(root.right)
                else:
                    return False
            elif root.left and not root.right:
                if root.left.val<root.val:
                    return dfs(root.left)
                else:
                    return False
            elif root.left == None and root.right == None:
                return True
            return False
        return dfs(root)
