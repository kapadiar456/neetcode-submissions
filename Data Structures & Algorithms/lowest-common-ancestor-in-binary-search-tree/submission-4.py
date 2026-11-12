# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def lca(r, p, q):
            print(r.val)
            if p.val<=r.val<=q.val or (r.val==p.val and r.val>q.val) or (r.val==q.val and r.val<p.val):
                return r
            elif p.val<r.val and q.val<r.val:
                return lca(r.left, p, q)
            else:
                return lca(r.right, p, q)
        return lca(root, p ,q)
