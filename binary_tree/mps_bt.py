# 124. Binary Tree Maximum Path Sum (Hard)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float('-inf')
        
        def dfs(root):
            nonlocal res
            if not root:
                return 0

            cur = root.val
            left = dfs(root.left)
            right = dfs(root.right)

            extendableSum = max(cur, cur + left, cur + right)
            maxSum = max(extendableSum, cur + left + right)
            if res < maxSum:
                res = maxSum 
            
            return extendableSum
        
        dfs(root)
        return res