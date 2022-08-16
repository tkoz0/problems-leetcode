class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        R = len(matrix)
        C = len(matrix[0])
        ret = [matrix[0][0]]
        r,c = 0,0
        matrix[r][c] = 101
        while len(ret) < R*C:
            while c+1 < C and matrix[r][c+1] != 101:
                c += 1
                ret.append(matrix[r][c])
                matrix[r][c] = 101
            while r+1 < R and matrix[r+1][c] != 101:
                r += 1
                ret.append(matrix[r][c])
                matrix[r][c] = 101
            while c-1 >= 0 and matrix[r][c-1] != 101:
                c -= 1
                ret.append(matrix[r][c])
                matrix[r][c] = 101
            while r-1 >= 0 and matrix[r-1][c] != 101:
                r -= 1
                ret.append(matrix[r][c])
                matrix[r][c] = 101
        return ret
