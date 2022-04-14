# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ret = []
        path = []
        def recur(n):
            if n:
                path.append(str(n.val))
                if not n.left and not n.right:
                    ret.append('->'.join(path))
                recur(n.left)
                recur(n.right)
                path.pop()
        recur(root)
        return ret
