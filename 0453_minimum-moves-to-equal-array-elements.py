class Solution:
    def minMoves(self, nums: List[int]) -> int:
        m=min(nums)
        return sum(n-m for n in nums)
