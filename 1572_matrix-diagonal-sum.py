class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        s = sum(mat[i][i]+mat[n-1-i][i] for i in range(n))
        if n%2==1:
            s -= mat[n//2][n//2]
        return s
