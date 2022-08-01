class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ''
        while all(len(s) > 0 for s in strs):
            c = strs[0][0]
            if all(s[0] == c for s in strs):
                prefix += c
                strs = [s[1:] for s in strs]
            else:
                break
        return prefix
