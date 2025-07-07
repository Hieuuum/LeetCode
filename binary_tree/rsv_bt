# 199. Binary Tree Right Side View (Medium)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
            
        curLvl, nxtLvl = collections.deque(), collections.deque()
        res = []

        nxtLvl.append(root)

        while nxtLvl:
            curLvl, nxtLvl = nxtLvl, curLvl
            if curLvl:
                res.append(curLvl[-1].val)
            while curLvl:
                cur = curLvl.popleft()
                if cur.left:
                    nxtLvl.append(cur.left)
                if cur.right:
                    nxtLvl.append(cur.right)
            
        return res