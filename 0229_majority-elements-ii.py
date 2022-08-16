class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n1,c1 = 1,0
        n2,c2 = 2,0
        for n in nums:
            if n == n1: # current majority candidates
                c1 += 1
            elif n == n2:
                c2 += 1
            elif c1 == 0: # assign new majority candidate
                n1,c1 = n,1
            elif c2 == 0:
                n2,c2 = n,1
            else:
                c1 -= 1
                c2 -= 1
            #print(n1,c1,n2,c2)
        ret = []
        maj = len(nums)//3
        if nums.count(n1) > maj:
            ret.append(n1)
        if nums.count(n2) > maj:
            ret.append(n2)
        return ret
