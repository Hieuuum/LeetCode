# 143. Reorder Linked List (Medium)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        cur = slow.next
        slow.next = prev = None

        while cur:
            temp = cur.next
            cur.next = prev
            prev, cur = cur, temp
        
        l, r = head, prev
        while l and r:
            tempL, tempR = l.next, r.next
            l.next = r
            r.next = tempL
            l, r = tempL, tempR