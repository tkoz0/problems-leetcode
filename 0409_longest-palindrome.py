class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = dict()
        for c in s:
            if c not in freq:
                freq[c] = 0
            freq[c] += 1
        ret = sum(freq[v]-(freq[v]%2) for v in freq)
        if any(freq[v]%2 for v in freq):
            ret += 1
        return ret
