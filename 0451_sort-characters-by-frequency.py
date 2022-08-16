class Solution:
    def frequencySort(self, s: str) -> str:
        freq = dict()
        for c in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789':
            freq[c] = 0
        for c in s:
            freq[c] += 1
        order = sorted(freq.items(),key=lambda x:-x[1])
        ret = ''
        for c,f in order:
            ret += c*f
        return ret
