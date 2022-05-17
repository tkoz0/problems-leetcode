# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        answer = None
        def recur(origroot,clonedroot):
            nonlocal answer
            if origroot is target:
                answer = clonedroot
            if origroot.left:
                recur(origroot.left,clonedroot.left)
            if origroot.right:
                recur(origroot.right,clonedroot.right)
        recur(original,cloned)
        return answer
