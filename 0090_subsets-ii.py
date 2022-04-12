class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        freq = dict()
        for n in nums:
            if n not in freq:
                freq[n] = 0
            freq[n] += 1
        ret = []
        def recur(freql,fi,inter):
            if fi == len(freql):
                ret.append(inter)
            else:
                n,c = freql[fi]
                for i in range(c+1):
                    recur(freql,fi+1,inter+[n]*i)
        recur(list(freq.items()),0,[])
        return ret
