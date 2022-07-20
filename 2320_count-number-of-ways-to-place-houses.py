class Solution:
    def countHousePlacements(self, n: int) -> int:
        ways = [1,2,3]
        while len(ways) <= n:
            ways.append(ways[-1]+ways[-2])
        return (ways[n]**2)%(10**9+7)
