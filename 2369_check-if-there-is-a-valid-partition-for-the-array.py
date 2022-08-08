class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        dp1 = [False]*(1+len(nums)) # if end with [x,x]
        dp2 = [False]*(1+len(nums)) # if end with [x,x,x]
        dp3 = [False]*(1+len(nums)) # if end with [x,x+1,x+2]
        dp1[0] = dp2[0] = dp3[0] = True
        if nums[0] == nums[1]:
            dp1[2] = True
        for i in range(2,len(nums)):
            dp1[i+1] = (nums[i] == nums[i-1]) and (dp1[i-1] or dp2[i-1] or dp3[i-1])
            dp2[i+1] = (nums[i] == nums[i-1] == nums[i-2]) and (dp1[i-2] or dp2[i-2] or dp3[i-2])
            dp3[i+1] = (nums[i]-2 == nums[i-1]-1 == nums[i-2]) and (dp1[i-2] or dp2[i-2] or dp3[i-2])
        return dp1[-1] or dp2[-1] or dp3[-1]
