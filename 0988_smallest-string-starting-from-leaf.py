# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        def cmp(a,b):
            i1,i2 = len(a)-1,len(b)-1
            while i1 >= 0 and i2 >= 0:
                if a[i1] > b[i2]:
                    return False
                if a[i1] < b[i2]:
                    return True
                i1 -= 1
                i2 -= 1
            return i1 < i2
        best = [26]
        path = []
        def recur(n):
            nonlocal best
            if n:
                path.append(n.val)
                if not n.left and not n.right and cmp(path,best):
                    best = path[:]
                recur(n.left)
                recur(n.right)
                path.pop()
        recur(root)
        return ''.join(chr(ord('a')+c) for c in best)[::-1]
