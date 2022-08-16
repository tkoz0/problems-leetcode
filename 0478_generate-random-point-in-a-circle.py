import random,math
class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.xc = x_center
        self.yc = y_center
        self.r = radius

    def randPoint(self) -> List[float]:
        while True:
            dx,dy = 2*self.r*(random.random()-0.5),2*self.r*(random.random()-0.5)
            if dx**2+dy**2 <= self.r**2:
                return [self.xc+dx,self.yc+dy]


# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()
