class Solution:
    def climbStairs(self, n: int) -> int:
        ways = [1,1]
        while len(ways) <= n:
            ways.append(ways[-1]+ways[-2])
        return ways[n]
