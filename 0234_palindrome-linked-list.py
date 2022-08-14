# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        a = head
        b = head.next
        odd = True
        while b:
            a = a.next
            b = b.next
            if b:
                b = b.next
            else:
                odd = False
        # reverse everything before a
        e = a
        p = head
        while p is not a:
            n = p.next
            p.next = e
            e = p
            p = n
        if odd:
            a = a.next
        # now e,a should correspond to equal elements
        while a:
            if e.val != a.val:
                return False
            a = a.next
            e = e.next
        return True
