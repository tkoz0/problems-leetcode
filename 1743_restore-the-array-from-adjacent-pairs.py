class Solution:
    def removepath(self, adj: Dict[int,Dict[int,int]]) -> List[int]:
        path = [next(iter(adj))]
        cur = next(iter(adj[path[0]]))
        adj[path[0]][cur] -= 1
        if adj[path[0]][cur] == 0:
            del adj[path[0]][cur]
            if len(adj[path[0]]) == 0:
                del adj[path[0]]
        adj[cur][path[0]] -= 1
        if adj[cur][path[0]] == 0:
            del adj[cur][path[0]]
            if len(adj[cur]) == 0:
                del adj[cur]
        while cur != path[0]:
            path.append(cur)
            cur = next(iter(adj[cur]))
            adj[path[-1]][cur] -= 1
            if adj[path[-1]][cur] == 0:
                del adj[path[-1]][cur]
                if len(adj[path[-1]]) == 0:
                    del adj[path[-1]]
            adj[cur][path[-1]] -= 1
            if adj[cur][path[-1]] == 0:
                del adj[cur][path[-1]]
                if len(adj[cur]) == 0:
                    del adj[cur]
        return path
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        adj = dict() # num -> adjnum:count mapping
        for u,v in adjacentPairs: # make mapping
            if u not in adj:
                adj[u] = dict()
            if v not in adj:
                adj[v] = dict()
            if v not in adj[u]:
                adj[u][v] = 0
            if u not in adj[v]:
                adj[v][u] = 0
            adj[u][v] += 1
            adj[v][u] += 1
        ret = []
        deg = dict() # num -> graph degree
        for u in adj:
            deg[u] = sum(adj[u].values())
        odds = [u for u in deg if deg[u] % 2 == 1]
        assert len(odds) == 0 or len(odds) == 2
        if len(odds) == 2: # add edge so eulerian circuit exists
            u,v = odds
            if v not in adj[u]:
                adj[u][v] = 0
            if u not in adj[v]:
                adj[v][u] = 0
            adj[u][v] += 1
            adj[v][u] += 1
            removeedge = [u,v]
        else:
            removeedge = None
        # find eulerian circuit, store in ret
        ##
        ret = self.removepath(adj)
        while len(adj) > 0:
            p = self.removepath(adj)
            for i in range(len(ret)):
                if ret[i] == p[0]:
                    ret = ret[:i] + p + ret[i+1:]
        print(adjacentPairs)
        print(ret)
        print(removeedge)
        ##
        # make sure this extra edge is cut
        if removeedge is not None:
            cut = [ret[0],ret[-1]]
            removeedge2 = removeedge[::-1]
            if cut == removeedge or cut == removeedge2:
                pass # cut is what we need
            else:
                # find the consecutive elements and adjust the cut
                i = None
                for j in range(len(ret)-1):
                    newcut = [ret[j],ret[j+1]]
                    if newcut == removeedge or newcut == removeedge2:
                        i = j
                        break
                assert i is not None
                print(i)
                ret = ret[i+1:] + ret[:i+1]
                print(ret)
        return ret
