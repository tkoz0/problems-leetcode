class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best = nums[0]
        current = nums[0]
        if current < 0:
            current = 0
        for n in nums[1:]:
            current += n
            best = max(best,current)
            if current < 0:
                current = 0
        return best
