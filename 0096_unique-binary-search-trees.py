class Solution:
    def numTrees(self, n: int) -> int:
        dp = [1]
        while len(dp) <= n:
            m = len(dp)
            dp.append(0)
            for i in range(m):
                l = i
                r = m-1-i
                dp[-1] += dp[l]*dp[r]
        return dp[n]
