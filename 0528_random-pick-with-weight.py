import random
class Solution:

    def __init__(self, w: List[int]):
        self.cumsum = [0]*(len(w))
        s = 0
        for i,n in enumerate(w):
            s += n
            self.cumsum[i] = s
        print(self.cumsum)

    def pickIndex(self) -> int:
        # binary search how many <= random number
        r = random.randint(0,self.cumsum[-1]-1)
        lo,hi = 0,len(self.cumsum)
        while lo<hi:
            mid=(lo+hi)//2
            if self.cumsum[mid] <= r:
                lo = mid+1
            else:
                hi = mid
        print(r,lo)
        return lo


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
