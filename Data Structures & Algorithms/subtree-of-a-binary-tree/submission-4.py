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
            

        def dfs(root, sub):
            if root == None:
                return
            val = False
            if root.val == sub.val:
                val = compare(root, sub)
            left = dfs(root.left, sub)
            right = dfs(root.right, sub)
            if left == True or right == True or val == True:
                return True
            else:
                return False
        sub  = subRoot
        return dfs(root, sub)

            