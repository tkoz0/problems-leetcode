# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if head:
            if not head.next:
                return TreeNode(head.val)
            prehead = ListNode(None,head)
            nm1 = prehead # nm1 = node before mid
            nm2 = head # nm2 = mid node
            nend = head.next
            while nend:
                nm1 = nm1.next
                nm2 = nm2.next
                nend = nend.next
                if nend:
                    nend = nend.next
            nm1.next = None
            ret = TreeNode(nm2.val,self.sortedListToBST(head),self.sortedListToBST(nm2.next))
            nm1.next = nm2
            return ret
        return None
