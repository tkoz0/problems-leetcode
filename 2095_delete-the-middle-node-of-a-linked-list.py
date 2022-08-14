# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return None
        a = head
        aprev = None
        b = head.next
        while b:
            aprev = a
            a = a.next
            b = b.next
            if b:
                b = b.next
        aprev.next = a.next
        return head
