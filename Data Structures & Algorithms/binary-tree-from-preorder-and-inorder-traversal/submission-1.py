# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#             0
#         1       3
#             2       4
# pre = 0,1,3,2,4
# in = 1,0,2,3,4

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        hashmap = defaultdict(int)
        for i in range(len(inorder)):
            hashmap[inorder[i]] = i
        self.index = 0
        def dfs(tempPreorder, l, r):
            if l>r:
                return None
            newNode = TreeNode(tempPreorder[self.index])
            self.index+=1
            print(newNode.val)
            index = hashmap[newNode.val]
            print(index)
            newNode.left = dfs(tempPreorder[l :index+1], 0, index+1)
            newNode.right = dfs(tempPreorder[index: r], index, len(preorder)-1)
            return newNode
        return dfs(preorder, 0, len(preorder)-1)