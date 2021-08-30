# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        xInfo = self.levelAndParent(root,x,0,None)
        yInfo = self.levelAndParent(root,y,0,None)
        return xInfo[0] == yInfo[0] and xInfo[1] != yInfo[1]
    def levelAndParent(self, root: Optional[TreeNode], x: int, level: int, parent: Optional[TreeNode]) -> Tuple[int,TreeNode]:
        if not root: return (-1,None) # -1 means x not found
        print(root.val,x)
        if root.val == x:
            return (level,parent)
        left = self.levelAndParent(root.left,x,level+1,root)
        right = self.levelAndParent(root.right,x,level+1,root)
        if left[0] != -1:
            return left
        if right[0] != -1:
            return right
        return (-1,None)
