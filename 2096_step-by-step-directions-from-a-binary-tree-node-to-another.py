# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        s = None
        t = None
        parent = dict() # val -> TreeNode
        def find(p,r):
            nonlocal s,t
            if r:
                parent[r.val] = p
                if r.val == startValue:
                    s = r
                if r.val == destValue:
                    t = r
                find(r,r.left)
                find(r,r.right)
        find(None,root)
        spath = [s]
        tpath = [t]
        while parent[spath[-1].val]:
            spath.append(parent[spath[-1].val])
        while parent[tpath[-1].val]:
            tpath.append(parent[tpath[-1].val])
        spath = spath[::-1] # root to node paths
        tpath = tpath[::-1]
        ret = ''
        if t in spath: # t is ancestor of s
            while spath[-1] is not t:
                ret += 'U'
                spath.pop()
        elif s in tpath: # s is ancestor of t
            while tpath[-1] is not s:
                n = tpath.pop()
                if tpath[-1].left == n:
                    ret = 'L'+ret
                else:
                    ret = 'R'+ret
        else: #  find common ancestor
            i = 0
            while spath[i] == tpath[i]:
                i += 1
            ancestor = spath[i-1]
            n = t
            while n != ancestor:
                n2 = parent[n.val]
                if n2.left == n:
                    ret = 'L'+ret
                else:
                    ret = 'R'+ret
                n = n2
            n = s
            while n != ancestor:
                n = parent[n.val]
                ret = 'U'+ret
        return ret
