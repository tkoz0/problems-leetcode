# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ptr1,ptr2 = l1,l2
        result_head = ListNode() # dummy temporary node
        ptr = result_head
        while ptr1:
            if ptr2: # both nonempty
                if ptr1.val < ptr2.val:
                    ptr.next = ptr1
                    ptr = ptr.next
                    ptr1 = ptr1.next
                else:
                    ptr.next = ptr2
                    ptr = ptr.next
                    ptr2 = ptr2.next
            else: # only ptr1 (possibly)
                ptr.next = ptr1
                break
        # only ptr2 (possibly)
        if ptr2:
            ptr.next = ptr2
        return result_head.next
