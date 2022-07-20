class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        best = [nums[0],nums[1]]
        for i in range(2,len(nums)):
            best.append(max(best[-1],nums[i]+max(best[:-1])))
        print(best)
        return max(best)
