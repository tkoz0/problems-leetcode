class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq = dict()
        for n in arr:
            if n not in freq:
                freq[n] = 0
            freq[n] += 1
        l = [n for n in freq if n == freq[n]]
        return max(l) if l else -1
