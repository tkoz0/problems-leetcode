# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        found = False
        def recur(n,s):
            nonlocal found
            if found: return
            if n:
                s += n.val
                if not n.left and not n.right and s == targetSum:
                    found = True
                else:
                    recur(n.left,s)
                    recur(n.right,s)
        recur(root,0)
        return found
