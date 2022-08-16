import random
class LC528edit: # copied from previous solution

    def __init__(self, w: List[int]):
        self.cumsum = [0]*(len(w))
        s = 0
        for i,n in enumerate(w):
            s += n
            self.cumsum[i] = s
        #print(self.cumsum)

    def pickIndex(self) -> List[int]: # -> randnum,original-prevs
        # binary search how many <= random number
        r = random.randint(0,self.cumsum[-1]-1)
        lo,hi = 0,len(self.cumsum)
        while lo<hi:
            mid=(lo+hi)//2
            if self.cumsum[mid] <= r:
                lo = mid+1
            else:
                hi = mid
        #print(r,lo)
        return lo,r-(self.cumsum[lo-1] if lo>0 else 0)

class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        weights = [(x-a+1)*(y-b+1) for a,b,x,y in rects]
        self.lc528e = LC528edit(weights)

    def pick(self) -> List[int]:
        r,o = self.lc528e.pickIndex()
        a,b,x,y = self.rects[r]
        assert 0<=o<(x-a+1)*(y-b+1)
        dy,dx = divmod(o,x-a+1)
        assert a<=a+dx<=x and b<=b+dy<=y
        return [a+dx,b+dy]


# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()
