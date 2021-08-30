class Solution:
    def reverse(self, x: int) -> int:
        sign = x//abs(x) if x != 0 else 0
        rev = self.revPositive(abs(x))
        ret = sign*rev
        if ret < -2**31 or ret >= 2**31:
            ret = 0
        return ret
    def revPositive(self, x: int) -> int:
        r = 0
        while x:
            r = 10*r + (x%10)
            x //= 10
        return r
