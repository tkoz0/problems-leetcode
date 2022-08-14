# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        i = 0
        p = head
        while p:
            p = p.next
            i += 1
        i -= n
        pprev = None
        p = head
        if i <= 0:
            return head.next
        while i > 0:
            i -= 1
            pprev = p
            p = p.next
        pprev.next = p.next
        return head
