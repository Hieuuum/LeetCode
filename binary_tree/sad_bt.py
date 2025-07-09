# 297. Serialize and Deserialize Binary Tree (Hard)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []
        curLvl = collections.deque()
        nxtLvl = collections.deque()
        nxtLvl.append(root)

        while nxtLvl:
            curLvl, nxtLvl = nxtLvl, curLvl
            while curLvl:
                cur = curLvl.popleft()
                if not cur:
                    res.append("N")
                else:
                    res.append(str(cur.val))
                    nxtLvl.append(cur.left)
                    nxtLvl.append(cur.right)

        return ",".join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        vals = data.split(",")
        TreeNodes = []
        if vals[0] == "N":
            return None

        root = TreeNode(int(vals[0]))
        queue = deque([root])
        i = 1

        while queue:
            cur = queue.popleft()
            if vals[i] != "N":
                cur.left = TreeNode(int(vals[i]))
                queue.append(cur.left)
            i += 1
            if vals[i] != "N":
                cur.right = TreeNode(int(vals[i]))
                queue.append(cur.right)
            i += 1

        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
