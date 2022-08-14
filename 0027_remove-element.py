class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        while i < len(nums) and nums[i] != val:
            i += 1
        for j in range(i,len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i
