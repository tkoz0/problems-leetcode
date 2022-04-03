class Solution:
    def maxNiceDivisors(self, primeFactors: int) -> int:
        # maximize 2^a * 3^b where 2a+3b <= primeFactors
        if primeFactors < 6: # special cases
            return [0,1,2,3,4,6][primeFactors]
        m = primeFactors % 3
        if m == 0:
            a=0
            b=primeFactors//3
        elif m == 1:
            a=2
            b=primeFactors//3-1
        else:
            a=1
            b=primeFactors//3
        return (pow(2,a,10**9+7)*pow(3,b,10**9+7)) % (10**9+7)
