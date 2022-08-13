class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1)+len(s2)!=len(s3):
            return False
        p = [[False]*(len(s2)+1) for _ in range(len(s1)+1)]
        # p[i][j] = is s3[:i+j] an interleaving of s1[:i] and s2[:j]
        for i in range(len(s1)+1):
            p[i][0] = s3[:i] == s1[:i]
        for j in range(len(s2)+1):
            p[0][j] = s3[:j] == s2[:j]
        for i in range(1,len(s1)+1):
            for j in range(1,len(s2)+1):
                p[i][j] = (s3[i+j-1] == s1[i-1] and p[i-1][j]) \
                    or (s3[i+j-1] == s2[j-1] and p[i][j-1])
        return p[-1][-1]
