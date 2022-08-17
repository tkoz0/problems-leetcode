# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        l = 0
        p = head
        while p:
            p = p.next
            l += 1
        k %= l
        i = l-k
        pprev = None
        p = head
        while i > 0:
            pprev = p
            p = p.next
            i -= 1
        # p is now at start of new list
        if not p:
            return head
        e = p
        while e.next:
            e = e.next
        # e is end of list to construct
        e.next = head # loop into cycle
        pprev.next = None # break cycle
        return p
