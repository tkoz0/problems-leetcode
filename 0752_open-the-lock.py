class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deads = set(tuple(map(int,s)) for s in deadends)
        targ = tuple(map(int,target))
        q = [(0,0,0,0)]
        v = set(deads)
        moves = 0
        while len(q):
            q2 = []
            for conf in q:
                if conf == targ:
                    return moves
                if conf in v:
                    continue
                v.add(conf)
                a,b,c,d = conf
                q2.append(((a+1)%10,b,c,d))
                q2.append(((a-1)%10,b,c,d))
                q2.append((a,(b+1)%10,c,d))
                q2.append((a,(b-1)%10,c,d))
                q2.append((a,b,(c+1)%10,d))
                q2.append((a,b,(c-1)%10,d))
                q2.append((a,b,c,(d+1)%10))
                q2.append((a,b,c,(d-1)%10))
            q = q2
            moves += 1
        return -1
