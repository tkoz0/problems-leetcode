import math
class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        divs = [2,3,5,7]
        primes = divs+[x for x in range(2,100) if not any(x%d==0 for d in divs)]
        primepi = len([p for p in primes if p <= n])
        return (math.factorial(primepi)*math.factorial(n-primepi))%(10**9+7)
