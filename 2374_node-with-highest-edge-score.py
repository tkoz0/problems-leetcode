class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        scores = [0]*len(edges)
        for i,j in enumerate(edges):
            scores[j] += i
        hi = 0
        for i in range(1,len(edges)):
            if scores[i] > scores[hi]:
                hi = i
        return hi
