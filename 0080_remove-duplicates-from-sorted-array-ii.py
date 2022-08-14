class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        count = 1
        for j in range(1,len(nums)):
            if nums[j] != nums[j-1]:
                nums[i] = nums[j]
                i += 1
                count = 1
            elif count < 2:
                    nums[i] = nums[j]
                    i += 1
                    count += 1
        return i
