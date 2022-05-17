class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.pq = [] # priority queue
        self.k = k
        for n in nums:
            i = len(self.pq)
            self.pq.append(n)
            while i > 0 and self.pq[(i-1)//2] > self.pq[i]:
                self.pq[(i-1)//2],self.pq[i] = self.pq[i],self.pq[(i-1)//2]
                i = (i-1)//2
        while len(self.pq) > k:
            self.pq[0] = self.pq.pop()
            i = 0
            while 2*i+1 < len(self.pq):
                si = i
                if self.pq[2*i+1] < self.pq[si]:
                    si = 2*i+1
                if 2*i+2 < len(self.pq) and self.pq[2*i+2] < self.pq[si]:
                    si = 2*i+2
                if si == i:
                    break
                self.pq[i],self.pq[si] = self.pq[si],self.pq[i]
                i = si

    def add(self, val: int) -> int:
        if len(self.pq) < self.k or val >= self.pq[0]:
            i = len(self.pq)
            self.pq.append(val)
            while i > 0 and self.pq[(i-1)//2] > self.pq[i]:
                self.pq[(i-1)//2],self.pq[i] = self.pq[i],self.pq[(i-1)//2]
                i = (i-1)//2
        while len(self.pq) > self.k:
            self.pq[0] = self.pq.pop()
            i = 0
            while 2*i+1 < len(self.pq):
                si = i
                if self.pq[2*i+1] < self.pq[si]:
                    si = 2*i+1
                if 2*i+2 < len(self.pq) and self.pq[2*i+2] < self.pq[si]:
                    si = 2*i+2
                if si == i:
                    break
                self.pq[i],self.pq[si] = self.pq[si],self.pq[i]
                i = si
        return self.pq[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
