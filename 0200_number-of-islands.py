class Solution:
    def dfs(self,visited:List[List[bool]],grid:List[List[str]],r:int,c:int):
        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]): return
        if grid[r][c] == "0": return
        if visited[r][c]: return
        visited[r][c] = True
        self.dfs(visited,grid,r+1,c)
        self.dfs(visited,grid,r,c+1)
        self.dfs(visited,grid,r-1,c)
        self.dfs(visited,grid,r,c-1)
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = [[False]*len(grid[0]) for _ in range(len(grid))]
        islands = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "0": continue
                if visited[r][c]: continue
                self.dfs(visited,grid,r,c)
                islands += 1
        return islands
