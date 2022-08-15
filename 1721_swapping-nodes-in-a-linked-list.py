# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        i = 1
        p = head
        while i < k:
            p = p.next
            i += 1
        j = i
        p2 = p
        while p2:
            p2 = p2.next
            j += 1
        j -= k
        i = 1
        p2 = head
        while i < j:
            p2 = p2.next
            i += 1
        p.val,p2.val = p2.val,p.val
        return head
