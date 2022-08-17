class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        freq = dict()
        for w in words:
            if w not in freq:
                freq[w] = 0
            freq[w] += 1
        ret = 0
        for w in list(freq.keys()):
            #print(w,ret,freq)
            if w not in freq:
                continue
            r = w[::-1]
            if r != w and r in freq:
                use = min(freq[w],freq[r])
                ret += 4*use
                freq[w] -= use
                freq[r] -= use
                if freq[w] == 0:
                    del freq[w]
                if freq[r] == 0:
                    del freq[r]
            elif r == w:
                use = freq[w]-(freq[w]%2)
                ret += 2*use
                freq[w] -= use
                if freq[w] == 0:
                    del freq[w]
        if any(freq[v] for v in freq if v == v[::-1]):
            ret += 2
        return ret
