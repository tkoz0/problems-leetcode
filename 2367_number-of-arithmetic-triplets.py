class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        ms = dict()
        for n in nums:
            if n not in ms:
                ms[n] = 0
            ms[n] += 1
        ret = 0
        for k in ms:
            if k+diff in ms and k+diff+diff in ms:
                ret += ms[k]*ms[k+diff]*ms[k+diff+diff]
        return ret
