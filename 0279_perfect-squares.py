class Solution:
    def numSquares(self, n: int) -> int:
        ps = [z*z for z in range(100,0,-1)]
        best = 10000
        def calc(s,i,l): # recurse largest square to smallest
            nonlocal best
            if s == 0: # reached sum
                best = min(best,l)
                return
            while i < len(ps): # try adding a square
                if ps[i] > s: # too big
                    i += 1
                    continue
                if l+s//ps[i]>best: # too small
                    break
                calc(s-ps[i],i,l+1)
                i += 1
        calc(n,0,0)
        return best
