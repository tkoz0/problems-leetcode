class Solution:
    def integerBreak(self, n: int) -> int:
        prod = [1]*(n+1)
        for i in range(2,n+1):
            for a in range(1,i): # first number
                newprod1 = a*prod[i-a]
                newprod2 = a*(i-a) # split into 2 nums
                if newprod1 > prod[i]:
                    prod[i] = newprod1
                if newprod2 > prod[i]:
                    prod[i] = newprod2
        return prod[n]
