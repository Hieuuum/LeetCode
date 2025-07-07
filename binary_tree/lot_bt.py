# 102. Binary Tree Level Order Traversal (Medium)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        curLvl = collections.deque()
        nxtLvl = collections.deque()
        res = []

        nxtLvl.append(root)

        while nxtLvl:
            curLvl, nxtLvl = nxtLvl, curLvl
            curLvlVal = []

            while curLvl:
                cur = curLvl.popleft()
                if cur:
                    curLvlVal.append(cur.val)
                    nxtLvl.append(cur.left)
                    nxtLvl.append(cur.right)

            if curLvlVal:
                res.append(curLvlVal)

        return res
        
        