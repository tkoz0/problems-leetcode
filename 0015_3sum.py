class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # make a multiset (num -> freq (freq >= 1))
        nums2 = dict()
        for n in nums:
            if n not in nums2:
                nums2[n] = 0
            nums2[n] += 1
        ret = set()
        for n1 in nums2: # first number
            nums2[n1] -= 1
            for n2 in nums2: # second number
                if nums2[n2] == 0:
                    continue
                nums2[n2] -= 1
                # see if 3rd number is available
                n3 = -(n1+n2)
                if n3 in nums2 and nums2[n3] > 0:
                    # sort because (-1,0,1) and (1,0,-1) are the same
                    ret.add(tuple(sorted((n1,n2,n3))))
                nums2[n2] += 1
            nums2[n1] += 1
        return [list(t) for t in ret]
