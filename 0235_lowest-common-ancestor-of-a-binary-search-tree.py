# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ppath = []
        qpath = []
        path = []
        def recur(r):
            nonlocal ppath,qpath,path
            if r:
                path.append(r)
                if r == p:
                    ppath = path[:]
                if r == q:
                    qpath = path[:]
                recur(r.left)
                recur(r.right)
                path.pop()
        recur(root)
        i = 0
        while i < len(ppath) and i < len(qpath) and ppath[i] == qpath[i]:
            i += 1
        return ppath[i-1]
