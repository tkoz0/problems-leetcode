# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        level_nodes = [root]
        level_values = [root.val]
        ret = []
        while level_nodes:
            ret.append(level_values)
            level_nodes2 = []
            level_values2 = []
            for node in level_nodes:
                assert node
                if node.left:
                    level_nodes2.append(node.left)
                    level_values2.append(node.left.val)
                if node.right:
                    level_nodes2.append(node.right)
                    level_values2.append(node.right.val)
            level_nodes = level_nodes2
            level_values = level_values2
        return ret
