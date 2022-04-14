# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ret = []
        path = []
        def recur(n,s):
            if n:
                s += n.val
                path.append(n.val)
                if not n.left and not n.right and s == targetSum:
                    ret.append(path[:])
                recur(n.left,s)
                recur(n.right,s)
                path.pop()
        recur(root,0)
        return ret
