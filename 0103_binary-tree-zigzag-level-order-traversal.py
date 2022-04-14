# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ret = []
        level = 0
        q = [root] if root else []
        while len(q):
            if level%2==0:
                ret.append([n.val for n in q])
            else:
                ret.append([n.val for n in q[::-1]])
            q2 = []
            for n in q:
                if n.left:
                    q2.append(n.left)
                if n.right:
                    q2.append(n.right)
            q = q2
            level += 1
        return ret
