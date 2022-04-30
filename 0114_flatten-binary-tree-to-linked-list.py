# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def reorder(r): # return end node
            if not r: return None
            if r.left:
                if r.right:
                    r.left,r.right = r.right,r.left
                    end = reorder(r.right)
                    end.right = r.left
                    r.left = None
                    return reorder(end.right)
                    # TODO put r.left in the end
                else:
                    r.right = r.left
                    r.left = None
                    return reorder(r.right)
            elif r.right:
                return reorder(r.right)
            else:
                return r
        reorder(root)
