class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        return int(100*sum(1 if c==letter else 0 for c in s)/len(s))
