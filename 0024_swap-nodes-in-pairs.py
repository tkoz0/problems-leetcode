# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        a = head
        b = head.next
        if not b:
            return head
        ret = b
        c = b.next
        b.next = a
        a.next = c
        prev = a
        a = c
        b = c
        if b:
            b = b.next
        while a and b:
            c = b.next
            prev.next = b
            b.next = a
            a.next = c
            prev = a
            a = c
            b = c
            if b:
                b = b.next
        return ret
