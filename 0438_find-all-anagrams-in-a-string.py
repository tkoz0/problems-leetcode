class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ret = []
        if len(s) < len(p):
            return []
        freq1 = dict()
        for c in p:
            if c not in freq1:
                freq1[c] = 0
            freq1[c] += 1
        freq2 = dict()
        for c in s[:len(p)]:
            if c not in freq2:
                freq2[c] = 0
            freq2[c] += 1
        if freq1 == freq2:
            ret.append(0)
        for i in range(len(p),len(s)):
            if s[i] not in freq2:
                freq2[s[i]] = 0
            freq2[s[i]] += 1
            freq2[s[i-len(p)]] -= 1
            if freq2[s[i-len(p)]] == 0:
                del freq2[s[i-len(p)]]
            if freq1 == freq2:
                ret.append(i-len(p)+1)
        return ret
