class Solution:
    def prime(self,n):
        if n < 4: return n == 2 or n == 3
        if n % 2 == 0: return False
        if n % 3 == 0: return False
        d = 5
        while d*d <= n:
            if n%d==0: return False
            if n%(d+2)==0: return False
            d += 6
        return True
    # digits = length of palindrome determiner part
    def do_len(self,digits,start,odd,numinput):
        for ld in range(int(str(start)[:1]),10):
            if ld not in [1,3,7,9]: continue
            for rp in range(10**(digits-1)):
                pp = ld*(10**(digits-1))+rp
                num = int(str(pp)+str(pp)[::-1][(1 if odd else 0):])
                if num >= numinput and self.prime(num): return num
    def primePalindrome(self, n: int) -> int:
        if n < 100:
            while True:
                if self.prime(n) and str(n) == str(n)[::-1]:
                    return n
                n += 1
        d = len(str(n))
        if d%2==0:
            ret = self.do_len(d//2,int(str(n)[:d//2]),False,n)
            if ret is not None: return ret
        else:
            ret = self.do_len((d+1)//2,int(str(n)[:(d+1)//2]),True,n)
            if ret is not None: return ret
        d += 1 # 2nd time
        if d%2==0:
            ret = self.do_len(d//2,10**(d//2-1),False,n)
            if ret is not None: return ret
        else:
            ret = self.do_len((d+1)//2,10**((d+1)//2-1),True,n)
            if ret is not None: return ret
        d += 1 # 3rd time should guarantee
        if d%2==0: return self.do_len(d//2,10**(d//2-1),False,n)
        else: return self.do_len((d+1)//2,10**((d+1)//2-1),True,n)
