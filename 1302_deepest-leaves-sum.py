# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        q = [root]
        s = root.val
        while len(q):
            q2 = []
            for n in q:
                if n.left:
                    q2.append(n.left)
                if n.right:
                    q2.append(n.right)
            q = q2
            if len(q):
                s = sum(n.val for n in q)
        return s
