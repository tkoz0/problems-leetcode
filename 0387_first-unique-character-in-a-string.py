class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = dict()
        for c in s:
            if c not in freq:
                freq[c] = 0
            freq[c] += 1
        for i,c in enumerate(s):
            if freq[c] == 1:
                return i
        return -1
