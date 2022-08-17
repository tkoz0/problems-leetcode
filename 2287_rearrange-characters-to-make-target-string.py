class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        freq = dict()
        for c in s:
            if c not in freq:
                freq[c] = 0
            freq[c] += 1
        if any(c not in freq for c in target):
            return 0
        tf = dict()
        for c in target:
            if c not in tf:
                tf[c] = 0
            tf[c] += 1
        return min(freq[c]//tf[c] for c in tf)
