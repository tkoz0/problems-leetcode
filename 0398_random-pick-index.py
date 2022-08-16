import random
class Solution:

    def __init__(self, nums: List[int]):
        self.data = dict() # num -> indexes
        for i,n in enumerate(nums):
            if n not in self.data:
                self.data[n] = []
            self.data[n].append(i)

    def pick(self, target: int) -> int:
        return random.choice(self.data[target])


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
