class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        # 1+2 + 2n
        # 1+2+3 + 3n
        # 1+2+3+4 + 4n
        # ...
        ways = 0
        i = 1
        while True:
            n -= i
            if n < 0: break
            if n % i == 0:
                ways += 1
            i += 1
        return ways
