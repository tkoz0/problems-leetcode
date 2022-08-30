class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        s = set(nums[0])
        for i in range(1,len(nums)):
            s &= set(nums[i])
        return sorted(s)
