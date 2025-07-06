# 110. Balanced Binary Tree (Easy)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        maxDiff = 0

        def dfs(root):
            nonlocal maxDiff
            if not root:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)

            maxDiff = max(maxDiff, abs(left - right))

            return 1 + max(left, right)
        
        dfs(root)
        return maxDiff <= 1


    