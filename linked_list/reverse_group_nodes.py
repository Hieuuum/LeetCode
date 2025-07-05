#25. Reverse Nodes in K-Group (Hard)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            kth = self.getKthNode(groupPrev, k)
            if not kth:
                break
            groupNext = kth.next

            # reverse group
            prev, cur = groupNext, groupPrev.next
            while cur != groupNext:
                temp = cur.next
                cur.next = prev
                prev, cur = cur, temp
            
            temp = groupPrev.next
            groupPrev.next = prev
            groupPrev = temp
        
        return dummy.next
        

    def getKthNode(self, cur, count):
        while cur and count > 0:
            cur = cur.next
            count -= 1
        return cur
