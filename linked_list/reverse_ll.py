# 206. Reverse Linked List (Easy)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return head
            
        cur = head
        before = None
        after = cur.next

        while cur:
            after = cur.next
            cur.next = before
            
            before = cur
            cur = after

        head = before

        return head
