class Solution:
    def tribonacci(self, n: int) -> int:
        if n < 3:
            return (n+1)//2
        a,b,c,i = 0,1,1,2
        while i < n:
            a,b,c,i = b,c,a+b+c,i+1
        return c
