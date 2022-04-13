# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        parent = dict() # val -> TreeNode
        depth = dict() # val -> depth
        def makeparent(n1,n2,d):
            if not n2: return
            parent[n2.val] = n1
            depth[n2.val] = d
            makeparent(n2,n2.left,d+1)
            makeparent(n2,n2.right,d+1)
        makeparent(None,root,0)
        maxdepth = max(depth.values())
        nodevals = set(v for v in depth if depth[v] == maxdepth)
        while len(nodevals) > 1:
            nodevals = set(parent[v].val for v in nodevals)
        v = list(nodevals)[0]
        if parent[v]:
            if parent[v].left and parent[v].left.val == v:
                return parent[v].left
            return parent[v].right
        return root
