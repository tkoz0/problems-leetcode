class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.q = [-1]*k
        self.i = 0
        self.l = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull(): return False
        self.q[(self.i+self.l)%self.k] = value
        self.l += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty(): return False
        self.i = (self.i+1)%self.k
        self.l -= 1
        return True

    def Front(self) -> int:
        return -1 if self.isEmpty() else self.q[self.i]

    def Rear(self) -> int:
        return -1 if self.isEmpty() else self.q[(self.i+self.l-1)%self.k]

    def isEmpty(self) -> bool:
        return self.l == 0

    def isFull(self) -> bool:
        return self.l == self.k


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
