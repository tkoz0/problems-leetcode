# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        def recur(n):
            if n.val > root.val:
                return n.val
            if n.left:
                a = recur(n.left)
                b = recur(n.right)
                if a != -1 and b != -1:
                    return min(a,b)
                return max(a,b)
            return -1
        return recur(root)
