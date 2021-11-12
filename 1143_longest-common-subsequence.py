class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        r1,r2 = [0]*(len(text2)+1), [0]*(len(text2)+1)
        for i in range(len(text1)):
            for j in range(len(text2)):
                r2[j+1] = 1+r1[j] if text1[i]==text2[j] else max(r1[j+1],r2[j])
            r1,r2 = r2,r1
        return r1[-1]
