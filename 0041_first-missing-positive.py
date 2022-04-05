class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            v = nums[i]
            # chain swaps to put 1,..,n at start of array in order
            # desire nums[i] = i+1
            while v in range(1,n+1) and v-1 != i:
                nums[i],nums[v-1] = nums[v-1],nums[i]
                if nums[i] == v: # terminate if cycle back to same
                    break
                v = nums[i]
        print(nums)
        # search for first missing positive
        i = 1
        while i <= n and nums[i-1] == i:
            i += 1
        return i
