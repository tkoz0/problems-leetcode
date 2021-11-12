class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        if len(s) == 1:
            return 1
        L0 = [1 for _ in range(len(s))] # L(0,0),...,L(n-1,n-1)
        L1 = [2 if s[i]==s[i+1] else 1 for i in range(len(s)-1)] # L(0,1),L(1,2),...
        dif = 1 # L2 represents problems L(x,x+dif), x=0,1,..
        while len(L1) > 1:
            dif += 1
            L2 = [2+L0[i+1] if s[i]==s[i+dif] else max(L1[i],L1[i+1]) for i in range(len(L1)-1)]
            L0,L1 = L1,L2
        return L1[0]
