class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        adj = [[] for _ in range(n)]
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        v = set(restricted)
        #print(adj)
        def dfs(n):
            if n in v:
                return
            v.add(n)
            #print(n)
            for z in adj[n]:
                dfs(z)
        dfs(0)
        return len(v)-len(restricted)
