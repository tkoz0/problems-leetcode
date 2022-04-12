# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def inorder(r):
            if not r:
                return []
            return inorder(r.left)+[r.val]+inorder(r.right)
        arr = inorder(root)
        def balance(arr,i,j):
            if i == j:
                return None
            mid = (i+j)//2
            return TreeNode(arr[mid],balance(arr,i,mid),balance(arr,mid+1,j))
        return balance(arr,0,len(arr))
