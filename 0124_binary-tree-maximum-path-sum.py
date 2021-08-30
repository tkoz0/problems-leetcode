# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # compute the DP tree
    # use it to compute best path sums
    # then the solution is the largest node value in the best path sums tree
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        dp = self.makeDPTree(root)
        ps = self.makeBestPathSums(root,dp)
        return self.maxNode(ps)
    # each node value is the largest sum path in its subtree
    def makeDPTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return None
        dp = TreeNode(None,self.makeDPTree(root.left),self.makeDPTree(root.right))
        leftSum = 0 if not dp.left else dp.left.val
        rightSum = 0 if not dp.right else dp.right.val
        dp.val = max(root.val,root.val+leftSum,root.val+rightSum)
        return dp
    # each node value is largest sum of a path going through itself in its subtree
    # the largest sum path will have a root so one of these will be the best
    # the sum is the root value plus the best path sums in its left and right subtrees
    # do not add the value of a subtree path if it is negative
    def makeBestPathSums(self, root: Optional[TreeNode], dp: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return None
        ps = TreeNode(None,self.makeBestPathSums(root.left,dp.left),self.makeBestPathSums(root.right,dp.right))
        # use 0 to ignore if subtree is empty
        bestLeft = 0 if not dp.left else dp.left.val
        bestRight = 0 if not dp.right else dp.right.val
        ps.val = root.val + max(0,bestLeft) + max(0,bestRight)
        return ps
    # max node in tree
    def maxNode(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        # only consider nonempty subtrees
        best = root.val
        if root.left:
            best = max(best,self.maxNode(root.left))
        if root.right:
            best = max(best,self.maxNode(root.right))
        return best
