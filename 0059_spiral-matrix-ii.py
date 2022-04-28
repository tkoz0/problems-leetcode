class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        mat = [[0]*n for _ in range(n)]
        mat[0][0] = 1
        r,c = 0,0
        while mat[r][c] != n*n:
            # right
            while c+1<n and mat[r][c+1] == 0:
                mat[r][c+1] = 1+mat[r][c]
                c += 1
            # down
            while r+1<n and mat[r+1][c] == 0:
                mat[r+1][c] = 1+mat[r][c]
                r += 1
            # left
            while c>0 and mat[r][c-1] == 0:
                mat[r][c-1] = 1+mat[r][c]
                c -= 1
            # up
            while r>0 and mat[r-1][c] == 0:
                mat[r-1][c] = 1+mat[r][c]
                r -= 1
        return mat
