class Solution:
    def isHappy(self, n: int) -> bool:
        def rep(z):
            ret=0
            while(z):
                z,r=divmod(z,10)
                ret+=r*r
            return ret
        while n != 1 and n != 89: # from project euler memory, all end in 1 or 89
            n=rep(n)
        return n == 1
