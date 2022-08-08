class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        r = dict() # value -> weight
        for v,w in items1+items2:
            if v not in r:
                r[v] = 0
            r[v] += w
        return [[v,r[v]] for v in sorted(r.keys())]
