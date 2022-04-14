class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = [set() for _ in range(numCourses)]
        for a,b in prerequisites:
            adj[a].add(b)
        ret = []
        for a,b in queries:
            q = set([a])
            isprereq = False
            while len(q):
                q2 = set()
                for c in q:
                    q2 |= adj[c]
                if b in q2:
                    isprereq = True
                    break
                q = q2
            ret.append(isprereq)
        return ret
