class Solution:
    def trailingZeroes(self, n: int) -> int:
        div = 5
        count = 0
        while div <= n:
            count += n//div
            div *= 5
        return count
