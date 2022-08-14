# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        ret = None
        retp = None
        p = head
        while p:
            if p.val != val:
                if not ret:
                    ret = retp = p
                else:
                    retp.next = p
                    retp = p
            p = p.next
        if retp:
            retp.next = None
        return ret
