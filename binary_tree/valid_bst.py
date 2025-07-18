# 98. Valid Binary Search Tree (Medium)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root, minVal, maxVal):
            if not root:
                return True
            if root.val <= minVal or root.val >= maxVal:
                return False
            
            return (dfs(root.left, minVal, root.val)
                    and dfs(root.right, root.val, maxVal))
        
        return dfs(root, float('-inf'), float('inf'))