# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head.next:
            return
        a = head
        aprev = None
        b = head.next
        while b:
            aprev = a
            a = a.next
            b = b.next
            if b:
                b = b.next
        aprev.next = None # head,a form 2 lists to pull from
        # length of a is >= length of head
        # reverse order of a
        e = None
        while a:
            n = a.next
            a.next = e
            e = a
            a = n
        # head,e form 2 lists to pull from, len(e) >= len(head)
        ret = head # value to return if this should return value
        retp = head
        head = head.next
        while e:
            retp.next = e
            retp = e
            e = e.next
            if head:
                retp.next = head
                retp = head
                head = head.next
        #return ret
