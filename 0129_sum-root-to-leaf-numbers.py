# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ret = 0
        def recur(n,s):
            nonlocal ret
            if n:
                s = 10*s+n.val
                if not n.left and not n.right:
                    ret += s
                recur(n.left,s)
                recur(n.right,s)
        recur(root,0)
        return ret
