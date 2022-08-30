class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        freq1 = dict()
        for c in s1:
            if c not in freq1:
                freq1[c] = 0
            freq1[c] += 1
        freq2 = dict()
        for c in s2[:len(s1)]:
            if c not in freq2:
                freq2[c] = 0
            freq2[c] += 1
        if freq1 == freq2:
            return True
        for i in range(len(s1),len(s2)):
            if s2[i] not in freq2:
                freq2[s2[i]] = 0
            freq2[s2[i]] += 1
            freq2[s2[i-len(s1)]] -= 1
            if freq2[s2[i-len(s1)]] == 0:
                del freq2[s2[i-len(s1)]]
            if freq1 == freq2:
                return True
        return False
