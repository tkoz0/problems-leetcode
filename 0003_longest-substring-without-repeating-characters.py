class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        best = 0
        for i in range(len(s)):
            chars = set()
            for j in range(i,len(s)):
                if s[j] not in chars:
                    chars.add(s[j])
                    best = max(best,j-i+1)
                else:
                    break
        return best
