class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        lost = dict() # player -> loss count
        for w,l in matches:
            if w not in lost:
                lost[w] = 0
            if l not in lost:
                lost[l] = 0
            lost[l] += 1
        return [sorted(p for p in lost if lost[p] == i) for i in [0,1]]
