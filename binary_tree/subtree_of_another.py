# 572. Subtree of Another Tree (Easy)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        elif not root:
            return False
        elif self.sameTree(root, subRoot):
            return True
        else:
            return (self.isSubtree(root.left, subRoot) or 
               self.isSubtree(root.right, subRoot))
    
    def sameTree(self, root, subRoot):
        if not root and not subRoot:
            return True
        elif root and subRoot and root.val == subRoot.val:
            return (self.sameTree(root.left, subRoot.left) and
                self.sameTree(root.right, subRoot.right))
        else:
            return False