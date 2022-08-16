class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0: return []
        ret = []
        rstart = 0
        while rstart < len(nums):
            rend = rstart+1
            while rend < len(nums) and nums[rend] == nums[rend-1]+1:
                rend += 1
            if rend == rstart+1:
                ret.append(f'{nums[rstart]}')
            else:
                ret.append(f'{nums[rstart]}->{nums[rend-1]}')
            rstart = rend
        return ret
