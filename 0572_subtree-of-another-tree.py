# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEqual(self, r1: Optional[TreeNode], r2: Optional[TreeNode]) -> bool:
        if r1 and r2:
            return r1.val == r2.val and self.isEqual(r1.left,r2.left) \
                and self.isEqual(r1.right,r2.right)
        return r1 == r2
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return root == subRoot
        return self.isEqual(root,subRoot) or self.isSubtree(root.left,subRoot) \
            or self.isSubtree(root.right,subRoot)
