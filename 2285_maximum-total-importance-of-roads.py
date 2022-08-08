class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        deg = dict() # city -> city degree
        for i in range(n):
            deg[i] = 0
        for a,b in roads:
            deg[a] += 1
            deg[b] += 1
        # sort by degree
        ret = 0
        for i,(city,degree) in enumerate(sorted(deg.items(), key = lambda x : x[1])):
            ret += (i+1)*degree
        return ret
