class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        # this is like pascal's triangle
        # a b c d e (1)
        # a+b b+c c+d d+e (1 1)
        # a+2b+c b+2c+d c+2d+e (1 2 1)
        # a+3b+3c+d b+3c+3d+e (1 3 3 1)
        # a+4b+6c+4d+e (1 4 6 4 1)
        # answer is sum (len(nums)-1 choose i) nums[i] for i=0 to i=n-1
        # compute these iteratively
        ret = nums[0]
        n = len(nums)
        nCi = 1 # kept mod 10
        e2,e5 = 0,0 # exponent of 2,5
        for i in range(1,n):
            # multiply by n-i / (i+1)
            m = n-i
            d = i
            if m != 0: # prevent infinite loop on last one
                while m % 2 == 0: e2 += 1; m //= 2
                while m % 5 == 0: e5 += 1; m //= 5
                while d % 2 == 0: e2 -= 1; d //= 2
                while d % 5 == 0: e5 -= 1; d //= 5
                # multiply and divide by using modular inverse
                nCi = (nCi * m * [0,1,0,7,0,0,0,3,0,9][d%10]) % 10
            # iterating pascal coeff = nCi * 2**e2 * 5**e5
            # mod 10 this is nCi * (1,2,4,8,6,2,4,8,6,...) * (1,5,5,...)
            # ignore the 1 for exponent 0 since that is handled separately
            #print(nCi,e2,e5,nums[i])
            if e2 == 0 or e5 == 0: # not divisible by 10
                t = nCi
                if e2 > 0: t *= [6,2,4,8][e2%4]
                if e5 > 0: t *= 5
                ret = (ret + t*nums[i]) % 10 # add
        return ret
