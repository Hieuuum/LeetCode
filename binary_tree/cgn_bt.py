# 1448. Count Good Nodes in Binary Tree (Medium)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(root, maxVal):
            count = 0

            if not root:
                return 0
            if root.val >= maxVal:
                count += 1
                maxVal = root.val

            return count + dfs(root.left, maxVal) + dfs(root.right, maxVal)
        
        return dfs(root, float('-inf'))