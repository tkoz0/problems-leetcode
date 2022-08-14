# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        mid,end = head,head
        while end:
            mid = mid.next
            end = end.next.next
        # reverse first half
        p = head
        e = mid # node to attach p before
        while p is not mid:
            n = p.next # next node
            p.next = e
            e = p
            p = n
        # now e[k],mid[k] correspond to sums
        best = e.val+mid.val
        while True:
            e = e.next
            mid = mid.next
            if not mid:
                break
            best = max(best,e.val+mid.val)
        return best
