# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        order = []
        def recur(r):
            nonlocal order
            if r:
                recur(r.left)
                order.append(r.val)
                recur(r.right)
        recur(root)
        if len(order) == 0: return None
        newroot = TreeNode(order[0])
        node = newroot
        for i in range(1,len(order)):
            node.right = TreeNode(order[i])
            node = node.right
        return newroot
