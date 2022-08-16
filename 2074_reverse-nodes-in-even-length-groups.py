# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        gstartprev = head
        gstart = head.next
        glen = 2
        while gstart:
            glast = gstart
            gend = gstart.next
            i = glen-1
            while gend and i > 0:
                glast = gend
                gend = gend.next
                i -= 1
            #if i > 0: # incomplete group
            #    break
            if (glen-i)%2 == 0: # reverse
                p = gstart
                e = gend
                while p is not gend:
                    n = p.next
                    p.next = e
                    e = p
                    p = n
                gstartprev.next = e
                gstartprev = gstart
            else:
                gstartprev = glast
            gstart = gend
            glen += 1
        return head
