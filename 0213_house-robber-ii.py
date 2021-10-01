class Solution:
    def dp(self,nums:List[int]) -> int:
        if len(nums) < 3:
            return max(nums)
        # solve linearly as if it does not wrap around
        didrob = [None]*len(nums)
        didntrob = [None]*len(nums)
        didrob[0] = nums[0]
        didntrob[0] = 0
        didrob[1] = nums[1]
        didntrob[1] = nums[0]
        for i in range(2,len(nums)):
            didntrob[i] = max(didntrob[i-1],didrob[i-1])
            didrob[i] = nums[i]+didntrob[i-1]
        return max(didrob[len(nums)-1],didntrob[len(nums)-1])
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 4:
            return max(nums)
        best = 0
        # one of [-1,0,1] must be robbed in an optimal solution
        best = max(best,nums[-1]+self.dp(nums[1:-2])) # -1
        best = max(best,nums[0]+self.dp(nums[2:-1])) # 0
        best = max(best,nums[1]+self.dp(nums[3:])) # 1
        return best
