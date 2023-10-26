class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums2 = set(nums) # remove dupes O(n)
        # make graph, O(1)*O(n)
        G = {n:(n-1 if n-1 in nums2 else None,
                n+1 if n+1 in nums2 else None) for n in nums2}
        # visited markers
        visit = {n:False for n in nums2}
        # bfs all graph components and save best size
        best = 0
        for n in nums2:
            if visit[n]:
                continue
            Q = [n]
            visit[n] = True
            size = 1
            while len(Q) > 0: # bfs next layer
                Q2 = []
                for m in Q:
                    u,v = G[m]
                    if u is not None and not visit[u]:
                        visit[u] = True
                        Q2.append(u)
                    if v is not None and not visit[v]:
                        visit[v] = True
                        Q2.append(v)
                Q = Q2
                size += len(Q)
            best = max(best,size)
        return best
