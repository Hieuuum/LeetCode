# 121. Merge Two Sorted Linked Lists (Easy)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        elif not list1:
            return list2
        elif not list2:
            return list1

        if list1.val > list2.val:
            list1, list2 = list2, list1
        
        cur = list1
        next1, next2 = list1.next, list2
        
        while next1 and next2:
            if next1.val < next2.val:
                cur.next = next1
                cur = next1
                next1 = next1.next
            else:
                cur.next = next2
                cur = next2
                next2 = next2.next
        
        if next1:
            cur.next = next1
        else:
            cur.next = next2
        
        return list1
                