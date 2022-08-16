class Solution:
    def getLucky(self, s: str, k: int) -> int:
        s = ''.join(str(' abcdefghijklmnopqrstuvwxyz'.index(c)) for c in s)
        s = int(s)
        for _ in range(k):
            s2 = 0
            s3 = s
            while s:
                s,r=divmod(s,10)
                s2+=r
            s=s2
        return s
