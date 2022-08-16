class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        snums = sorted(nums)
        med = snums[len(nums)//2] if len(nums)%2 else (snums[len(nums)//2]+snums[len(nums)//2-1])//2
        return sum(abs(n-med) for n in nums)
