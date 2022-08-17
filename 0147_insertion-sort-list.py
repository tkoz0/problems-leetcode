# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sorthead = head
        sorttail = head
        while sorttail.next:
            p = sorttail.next # insert this one
            i = None
            j = sorthead
            while j.val < p.val:
                i = j
                j = j.next
            if j is p: # insert at end
                sorttail = p
            elif not i: # insert at beginning
                sorttail.next = p.next
                p.next = sorthead
                sorthead = p
            else: # insert in middle
                sorttail.next = p.next
                i.next = p
                p.next = j
        return sorthead
