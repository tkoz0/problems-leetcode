# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        if not head:
            return [None]*k
        l = 0
        p = head
        while p:
            p = p.next
            l += 1
        ret = []
        pprev = None
        p = head
        while k > 0: # for each part
            ret.append(p) # push head of part
            size = (l+k-1)//k
            for _ in range(size): # skip part
                pprev = p
                p = p.next
            l -= size # length of remainder
            pprev.next = None # terminate part
            k -= 1
        return ret
