# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def compare(root, subRoot):
            if root == None and subRoot==None:
                return True
            elif ((root and subRoot == None) or (root==None and subRoot)):
                return False
            left = compare(root.left, subRoot.left)
            right = compare(root.right, subRoot.right)
            if left == True and right == True:
                return True
            else:
                return False
            

        def dfs(root):
            if root == None:
                return
            if root.val == subRoot.val:
                return compare(root, subRoot)
            left = dfs(root.left)
            right = dfs(root.right)
            if left == True or right == True:
                return True
            else:
                return False
        return dfs(root)

            