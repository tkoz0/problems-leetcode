class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        bit = 2**15
        root = 0
        while bit:
            if (root+bit)**2 <= num:
                root += bit
            bit //= 2
            if root**2 == num:
                return True
