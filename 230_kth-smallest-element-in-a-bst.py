# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        assert root and k >= 1
        n = self.countNodes(root.left)
        if k <= n:
            return self.kthSmallest(root.left,k)
        elif k > n+1:
            return self.kthSmallest(root.right,k-n-1)
        else: # k == n+1
            return root.val
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
