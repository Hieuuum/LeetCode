# 138. Copy Linked List with Random Pointer (Medium)

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        cur = head
        copy_dict = {None: None}
        while cur:
            copy_dict[cur] = Node(cur.val)
            cur = cur.next
        
        cur, copy = head, copy_dict[head]
        while cur:
            copy.next = copy_dict[cur.next]
            copy.random = copy_dict[cur.random]
            cur, copy = cur.next, copy.next
        
        return copy_dict[head]