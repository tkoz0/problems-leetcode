class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        a,b,i = 0,1,1
        while i < n:
            a,b,i = b,a+b,i+1
        return b
