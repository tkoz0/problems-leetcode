class Node:
    def __init__(self,v,p=None,ch=[]):
        self.v=v # number
        self.p=p # parent
        self.ch=[] # children
        self.h=0 # height, computed later
        self.lp=0 # rooted long path length
        self.deep=None # deepest child
class Solution:
    def makeTree(self,parent:int,node:Node,edgemap:Dict[int,List[int]]):
        for adj in edgemap[node.v]:
            if adj == parent: continue
            node.ch.append(Node(adj,node))
            self.makeTree(node.v,node.ch[-1],edgemap)
    def computeHeights(self,root:Node):
        if len(root.ch) == 0:
            root.h = 1
            root.lp = 1
            root.deep = root # itself if no children
        else:
            for ch in root.ch:
                self.computeHeights(ch)
            h = sorted(ch.h for ch in root.ch)
            hmax = max(h)
            root.h = 1+hmax
            if len(h) == 1:
                root.lp = 1+h[0]
            else:
                root.lp = 1+h[-1]+h[-2]
            # find deepest child
            for ch in root.ch:
                if ch.h == hmax:
                    root.deep = ch.deep
        #print(f'v={root.v},p={root.p.v if root.p else -1},ch={[ch.v for ch in root.ch]},h={root.h},lp={root.lp},deep={root.deep.v}')
    def findBestNode(self,root:Node) -> Node:
        # node with maximum lp value (longest rooted path length)
        if len(root.ch) == 0: return root
        lp = root.lp
        best = root
        for ch in root.ch:
            ch2 = self.findBestNode(ch)
            if ch2.lp > lp:
                lp = ch2.lp
                best = ch2
        return best
    def findRootedLongPath(self,root:Node) -> List[int]:
        if len(root.ch) == 0:
            return [root.v]
        h = sorted(ch.h for ch in root.ch)
        hd = dict() # height -> [child]
        for ch in root.ch:
            if ch.h not in hd: hd[ch.h] = []
            hd[ch.h].append(ch)
        if len(h) == 1: # follow deepest to root
            n = hd[h[-1]][0].deep
            path = [n.v]
            while n != root:
                n = n.p
                path.append(n.v)
            #print(f'path={path}')
            return path
        # follow 2 deepest to root, combine
        if len(hd[h[-1]]) >= 2:
            d1,d2 = hd[h[-1]][0].deep,hd[h[-1]][1].deep
        else:
            d1,d2 = hd[h[-1]][0].deep,hd[h[-2]][0].deep
        #print(f'd1.v={d1.v},d2.v={d2.v}')
        n = d1
        path1 = [n.v]
        while n != root:
            n = n.p
            path1.append(n.v)
        n = d2
        path2 = [n.v]
        while n != root:
            n = n.p
            path2.append(n.v)
        #print(f'path1={path1}')
        #print(f'path2={path2}')
        return path1[:-1]+path2[::-1]
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # (length based on number of nodes)
        # if longest path is even, it is unique, choose both center nodes
        # if longest path is odd, another longest may cross it, pick only center node
        # first build a tree with any root (choosing 0)
        # longest path is some root connected to its longest path down 1 or 2 subtrees
        edgemap = dict() # node -> [adjacent]
        for a in range(n):
            edgemap[a] = []
        for a,b in edges:
            edgemap[a].append(b)
            edgemap[b].append(a)
        root = Node(0)
        self.makeTree(-1,root,edgemap)
        self.computeHeights(root)
        path = self.findRootedLongPath(self.findBestNode(root))
        #print(path)
        if len(path) % 2 == 0:
            return [path[len(path)//2],path[len(path)//2-1]]
        return [path[len(path)//2]]
