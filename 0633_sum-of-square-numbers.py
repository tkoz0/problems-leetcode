import math
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        def is_sq(n):
            r = math.floor(math.sqrt(n))
            return r*r==n
        r = math.floor(math.sqrt(c))
        for i in range(r+1):
            if is_sq(c-i*i):
                return True
        return False
