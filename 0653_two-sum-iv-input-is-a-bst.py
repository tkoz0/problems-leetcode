# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        freq = dict()
        def recur(r):
            if not r: return
            recur(r.left)
            recur(r.right)
            if r.val not in freq:
                freq[r.val] = 0
            freq[r.val] += 1
        recur(root)
        for a in freq:
            if k-a in freq and (k-a!=a or freq[a]>1):
                return True
        return False
