class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # boyer-moore majority vote algorithm
        n1,c1 = nums[0],1
        i = 0
        for n in nums:
            if i == 0:
                n1 = n
                i = 1
            elif n1 == n:
                i += 1
            else:
                i -= 1
        return n1
