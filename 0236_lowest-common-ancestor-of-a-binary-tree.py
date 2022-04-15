# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        path = []
        ppath = []
        qpath = []
        nodemap = dict() # val -> TreeNode
        def recur(r):
            nonlocal ppath,qpath
            if r:
                nodemap[r.val] = r
                path.append(r.val)
                if r == p:
                    ppath = path[:]
                if r == q:
                    qpath = path[:]
                recur(r.left)
                recur(r.right)
                path.pop()
        recur(root)
        print(ppath,qpath)
        i = 0
        while i < len(ppath) and i < len(qpath) and ppath[i] == qpath[i]:
            i += 1
        if i == len(ppath):
            return nodemap[ppath[-1]]
        if i == len(qpath):
            return nodemap[qpath[-1]]
        a = ppath[i-1]
        n,i = root,1
        while n.val != a:
            if n.left and n.left.val == ppath[i]:
                n = n.left
            elif n.right and n.right.val == ppath[i]:
                n = n.right
            i += 1
        return n
