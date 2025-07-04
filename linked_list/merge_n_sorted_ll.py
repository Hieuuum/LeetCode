# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        dummy = ListNode(float('-inf'), lists[0])
        lists[0] = dummy

        while len(lists) > 1:
            cur1, cur2 = lists[0], lists.pop()
            while cur1.next and cur2:
                nxt1 = cur1.next

                if nxt1.val >= cur2.val:
                    temp = cur2.next
                    cur1.next = cur2
                    cur2.next = nxt1
                    cur2 = temp
                else:
                    cur1 = cur1.next
            
            if cur2:
                cur1.next = cur2
        
        return lists[0].next


        