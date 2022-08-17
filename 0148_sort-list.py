# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: # length 0 or 1
            return head
        # split in half
        left = head
        right = head
        fast = head.next
        while fast:
            rightprev = right
            right = right.next
            fast = fast.next
            if fast:
                fast = fast.next
        rightprev.next = None # break link
        # sort halves
        left = self.sortList(left)
        right = self.sortList(right)
        # merge
        if left.val < right.val:
            rethead = rettail = left
            left = left.next
        else:
            rethead = rettail = right
            right = right.next
        while left:
            if not right or left.val < right.val:
                rettail.next = left
                rettail = left
                left = left.next
            else:
                rettail.next = right
                rettail = right
                right = right.next
        rettail.next = right
        return rethead
