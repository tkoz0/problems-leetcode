# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        aprev = None
        a = head
        b = head
        while left > 1:
            aprev = a
            a = a.next
            b = b.next
            left -= 1
            right -= 1
        while right > 0: # has to move 1 past end
            b = b.next
            right -= 1
        e = b
        while a is not b:
            n = a.next
            a.next = e
            e = a
            a = n
        if aprev:
            aprev.next = e
            return head
        else:
            return e
