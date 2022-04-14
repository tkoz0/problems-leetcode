# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        level = 0
        q = [root]
        while len(q):
            parity = 1-(level%2)
            if any(n.val%2!=parity for n in q):
                return False
            if level%2==0 and any(q[i-1].val >= q[i].val for i in range(1,len(q))):
                return False
            if level%2==1 and any(q[i-1].val <= q[i].val for i in range(1,len(q))):
                return False
            q2 = []
            for n in q:
                if n.left:
                    q2.append(n.left)
                if n.right:
                    q2.append(n.right)
            q = q2
            level += 1
        return True
