class Solution:
    def repeatedCharacter(self, s: str) -> str:
        for i,c in enumerate(s):
            if c in s[:i]:
                return c
