class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l = min(len(word1),len(word2))
        ret = ''.join(word1[i//2] if i%2==0 else word2[i//2] for i in range(2*l))
        if len(word1) > l:
            ret += word1[l:]
        if len(word2) > l:
            ret += word2[l:]
        return ret
