class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        r,c = rStart,cStart
        ret = [[r,c]]
        z = 0 # step length
        while len(ret) < rows*cols:
            z += 1
            for _ in range(z):
                c += 1
                if 0 <= r < rows and 0 <= c < cols:
                    ret.append([r,c])
            for _ in range(z):
                r += 1
                if 0 <= r < rows and 0 <= c < cols:
                    ret.append([r,c])
            z += 1
            for _ in range(z):
                c -= 1
                if 0 <= r < rows and 0 <= c < cols:
                    ret.append([r,c])
            for _ in range(z):
                r -= 1
                if 0 <= r < rows and 0 <= c < cols:
                    ret.append([r,c])
        return ret
