# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ret = []
        def recur(node,level):
            if not node: return
            if level==len(ret):
                ret.append(node.val)
            recur(node.right,level+1)
            recur(node.left,level+1)
        recur(root,0)
        return ret
