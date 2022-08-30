class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ret = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])-1):
                if grid[r][c] != grid[r][c+1]:
                    ret += 1
            if grid[r][0]:
                ret += 1
            if grid[r][-1]:
                ret += 1
        for c in range(len(grid[0])):
            for r in range(len(grid)-1):
                if grid[r][c] != grid[r+1][c]:
                    ret += 1
            if grid[0][c]:
                ret += 1
            if grid[-1][c]:
                ret += 1
        return ret
