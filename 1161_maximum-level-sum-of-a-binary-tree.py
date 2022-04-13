# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        level = [root]
        i = 1
        bestlevel = 1
        bestsum = root.val
        while True:
            level2 = [n.left for n in level if n.left]+[n.right for n in level if n.right]
            if len(level2) == 0:
                break
            i += 1
            level2sum = sum(n.val for n in level2)
            if level2sum > bestsum:
                bestlevel = i
                bestsum = level2sum
            level = level2
        return bestlevel
