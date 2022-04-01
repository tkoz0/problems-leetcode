class Solution:
    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        half = (intLength+1)//2
        result = []
        for i in queries:
            i -= 1
            if i >= 9*10**(half-1):
                result.append(-1)
            else:
                r = 10**(half-1)+i
                s = str(r) + str(r)[::-1][0 if intLength % 2 == 0 else 1:]
                result.append(int(s))
        return result
