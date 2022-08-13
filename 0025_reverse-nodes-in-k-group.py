# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        p = head.next
        kk = k-1
        while kk > 0 and p:
            kk -= 1
            p = p.next
        if kk > 0: # not long enough to reverse
            return head
        tail_part = self.reverseKGroup(p,k) # apply to rest of list
        end_p = p
        p = head
        while p is not end_p:
            n = p
            p = p.next
            n.next = tail_part
            tail_part = n
        return tail_part

