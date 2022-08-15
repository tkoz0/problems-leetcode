# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        summing_node_prev = None
        summing_node = head
        itr_node = head.next
        while itr_node:
            while itr_node.val != 0:
                summing_node.val += itr_node.val
                itr_node = itr_node.next
            summing_node_prev = summing_node
            summing_node.next = itr_node
            summing_node = itr_node
            itr_node = itr_node.next
        summing_node_prev.next = None
        return head
