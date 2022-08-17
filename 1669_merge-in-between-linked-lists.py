# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        aprev = None
        aptr = list1
        for _ in range(a):
            aprev = aptr
            aptr = aptr.next
        bptr = aptr
        for _ in range(b-a):
            bptr = bptr.next
        aprev.next = list2
        p = list2
        while p.next:
            p = p.next
        p.next = bptr.next
        return list1
