class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        M = [[0]*n for _ in range(m)]
        for r,c in indices:
            for i in range(n):
                M[r][i] += 1
            for i in range(m):
                M[i][c] += 1
        return sum(sum(n%2 for n in row) for row in M)
