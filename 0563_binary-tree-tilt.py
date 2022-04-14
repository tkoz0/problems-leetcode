# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        def recur(r): # return (subtree sum, tilt sum)
            if not r: return (0,0)
            a,b = recur(r.left)
            c,d = recur(r.right)
            return (r.val+a+c,b+d+abs(a-c))
        return recur(root)[1]
