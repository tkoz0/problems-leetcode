# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        e = None
        p = head
        while p:
            n = p.next
            p.next = e
            e = p
            p = n
        return e
