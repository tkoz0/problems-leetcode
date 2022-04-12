class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0]:
            return -1
        n = len(grid)
        visited = [[False]*n for _ in range(n)]
        layer = set([(0,0)])
        visited[0][0] = True
        path = 1
        while (n-1,n-1) not in layer and len(layer):
            layer2 = set()
            for r,c in layer:
                for dr in range(-1,2):
                    for dc in range(-1,2):
                        rr,cc = r+dr,c+dc
                        if rr < 0 or cc < 0:
                            continue
                        if rr >= n or cc >= n:
                            continue
                        if visited[rr][cc]:
                            continue
                        if grid[rr][cc]:
                            continue
                        layer2.add((rr,cc))
                        visited[rr][cc] = True
            layer = layer2
            path += 1
        return path if (n-1,n-1) in layer else -1
