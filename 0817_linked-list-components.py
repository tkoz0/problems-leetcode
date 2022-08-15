# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        nums = set(nums)
        p = head
        count = 0
        component_size = 1
        while p:
            if p.val in nums:
                component_size += 1
                if not p.next or (p.val not in nums) or (p.next.val not in nums):
                    component_size = 0
                    count += 1
            else:
                component_size = 0
            p = p.next
        return count
