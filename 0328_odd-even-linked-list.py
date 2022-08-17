# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        oddend = head
        evenstart = evenend = head.next
        while evenend.next and evenend.next.next:
            a = evenend.next
            b = evenend.next.next
            oddend.next = a
            a.next = evenstart
            evenend.next = b
            oddend = a
            evenend = b
        if evenend.next: # extra odd
            oddend.next = evenend.next
            oddend.next.next = evenstart
        evenend.next = None
        return head
