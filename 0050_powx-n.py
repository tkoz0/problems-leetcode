class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return 1.0/self.myPow(x,-n)
        base = x
        result = 1.0
        while n:
            n,bit = divmod(n,2)
            if bit:
                result *= base
            base *= base
        return result
