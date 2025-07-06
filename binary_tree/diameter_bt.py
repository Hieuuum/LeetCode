# 543. Diameter of Binary Tree (Easy)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        self.dfs(root)

        return self.res
    
    def dfs(self, root):

        if not root:
            return 0
        
        left = self.dfs(root.left)
        right = self.dfs(root.right)

        self.res = max(self.res, left + right)

        return 1 + max(left, right)
