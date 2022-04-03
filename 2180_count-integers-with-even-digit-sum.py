class Solution:
    def countEven(self, num: int) -> int:
        return len([i for i in range(1,num+1) if sum(int(c) for c in str(i)) % 2 == 0])
