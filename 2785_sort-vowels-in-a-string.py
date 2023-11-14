class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = set('aeiouAEIOU')
        ss = sorted([c for c in s if c in vowels])
        ret = list(s)
        ssi = iter(ss)
        for i,c in enumerate(ret):
            if c in vowels:
                ret[i] = next(ssi)
        return ''.join(ret)
