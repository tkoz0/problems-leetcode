class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        ret = []
        for start,end in intervals:
            if len(ret):
                if start <= ret[-1][1]:
                    ret[-1][1] = max(ret[-1][1],end)
                else:
                    ret.append([start,end])
            else:
                ret.append([start,end])
        return ret
