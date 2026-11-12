# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSame(p, q):
            if p == None and q == None:
                return True
            if p==None:
                return False
            if q == None:
                return False
            if p.val != q.val:
                return False
            right = isSame(p.right, q.right)
            left = isSame(p.left, q.left)
            if left == True and right == True:
                return True
            else:
                return False
        def sub(r, s):
            if r == None:
                return False
            if r.val == s.val:
                return isSame(r, s)
            right = sub(r.right, s)
            left = sub(r.left, s)
            if left == True or right == True:
                return True
            else:
                return False
        return sub(root, subRoot)