class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        freq1 = dict()
        freq2 = dict()
        for n in nums1:
            if n not in freq1:
                freq1[n] = 0
            freq1[n] += 1
        for n in nums2:
            if n not in freq2:
                freq2[n] = 0
            freq2[n] += 1
        ret = []
        for n in freq1:
            if n in freq2:
                ret += [n]*min(freq1[n],freq2[n])
        return ret
