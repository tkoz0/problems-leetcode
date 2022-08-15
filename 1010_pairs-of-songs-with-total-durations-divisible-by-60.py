class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        counts = [0]*60
        for t in time:
            counts[t%60] += 1
        ret = counts[0]*(counts[0]-1)//2 + counts[30]*(counts[30]-1)//2
        for t in range(1,30):
            ret += counts[t]*counts[60-t]
        return ret
