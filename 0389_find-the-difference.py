class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        freq = dict()
        for c in t:
            if c not in freq:
                freq[c] = 0
            freq[c] += 1
        for c in s:
            freq[c] -= 1
            if freq[c] == 0:
                del freq[c]
        return list(freq.keys())[0]
