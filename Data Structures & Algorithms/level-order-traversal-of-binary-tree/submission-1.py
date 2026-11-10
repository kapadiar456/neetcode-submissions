# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        q.append(root)
        final = []
        while q:
            n = len(q)
            res = []
            for _ in range(n):
                node = q.popleft()
                if node:
                    q.append(node.left)
                    q.append(node.right)
                    res.append(node.val)
            if res:
                final.append(res)
        return final
            