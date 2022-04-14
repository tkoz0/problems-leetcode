# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def recur(a,b):
            if a > b:
                return [None]
            ret = []
            for i in range(a,b+1):
                L = recur(a,i-1)
                R = recur(i+1,b)
                ret += [TreeNode(i,l,r) for l in L for r in R]
            return ret
        return recur(1,n)
