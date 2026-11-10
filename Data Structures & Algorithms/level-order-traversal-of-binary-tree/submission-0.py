# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = deque()
        q.append(root)
        length=0
        res = [[root.val]]
        while q:
            newList = []
            while length > 0:
                node = q.popleft()
                print("node", node.val)
                print(node.val)
                if node.left:
                    q.append(node.left)
                    newList.append(node.left.val)
                if node.right:
                    q.append(node.right)
                    newList.append(node.right.val)
                length-=1
            if newList:
                res.append(newList)
            length = len(q)
        return res