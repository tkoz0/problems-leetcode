class Solution:
    def generator(self,nums,result=[]):
        if len(nums) == 0:
            yield result
        used = set()
        for i,num in enumerate(nums):
            if num in used: continue
            used.add(num)
            yield from self.generator(nums[:i]+nums[i+1:],result+[num])
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        return list(self.generator(nums))
