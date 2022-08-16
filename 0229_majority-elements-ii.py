class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if len(nums) < 3:
            return list(set(nums))
        n = len(nums)
        # medians can be done in linear time, don't feel like coding it
        # still not O(1) memory
        medm = sorted(nums)[n//2]
        medl = sorted(nums)[:n//2][(n//2)//2]
        medr = sorted(nums)[n//2:][(n//2)//2]
        countm = 0
        countl = 0
        countr = 0
        maj = n//3
        for z in nums:
            if z == medm: countm += 1
            if z == medl: countl += 1
            if z == medr: countr += 1
        ret = []
        if countm > maj: ret.append(medm)
        if countl > maj: ret.append(medl)
        if countr > maj: ret.append(medr)
        return list(set(ret))
