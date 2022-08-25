class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            groups = [s[a:a+k] for a in range(0,len(s),k)]
            sums = [sum(map(int,g)) for g in groups]
            s = ''.join(map(str,sums))
        return s
