# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # start result off with first node
        result = ListNode((l1.val + l2.val) % 10)
        resulthead = result # save for return value
        carry = (l1.val + l2.val) // 10
        l1 = l1.next
        l2 = l2.next
        while l1 and l2: # process corresponding nodes together
            result.next = ListNode((l1.val + l2.val + carry) % 10)
            result = result.next
            carry = (l1.val + l2.val + carry) // 10
            l1 = l1.next
            l2 = l2.next
        if l2: l1 = l2
        while l1: # remaining list if 1 is longer
            result.next = ListNode((l1.val + carry) % 10)
            result = result.next
            carry = (l1.val + carry) // 10
            l1 = l1.next
        if carry: # nonzero last carry requires extra node
            result.next = ListNode(carry)
        return resulthead
