# 235. Lowest Common Ancestor in Binary Search Tree (Medium)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        cur = root

        while cur:
            if cur.val < min(q.val, p.val):
                cur = cur.right
            elif cur.val > max(q.val, p.val):
                cur = cur.left
            else:
                return cur