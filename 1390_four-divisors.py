class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        sieve = [True]*100000
        sieve[0] = sieve[1] = False
        for i in range(2,317):
            if not sieve[i]: continue
            for j in range(i*i,100000,i):
                sieve[j] = False
        pl = [i for i,n in enumerate(sieve) if n]
        #print(pl)
        ps = set(pl)
        ret = 0
        # 3rd powers of primes have 4 divisors
        pow3 = {8: 15, 27: 40, 125: 156, 343: 400, 1331: 1464, 2197: 2380, 4913: 5220, 6859: 7240, 12167: 12720, 24389: 25260, 29791: 30784, 50653: 52060, 68921: 70644, 79507: 81400}
        for n in nums:
            if n in pow3: # check for 3rd power
                ret += pow3[n]
                continue
            for d in pl: # check for semiprime
                if d*d > n:
                    break
                if n % d == 0:
                    d2 = n//d
                    if d2 != d and d2 in ps:
                        ret += (d+1)*(d2+1)
                        #print(n,(d+1)*(d2+1))
                    else:
                        break
        return ret
