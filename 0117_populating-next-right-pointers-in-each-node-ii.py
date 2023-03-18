"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        level = [root]
        while len(level):
            for i in range(len(level)-1):
                level[i].next = level[i+1]
            level2 = []
            for node in level:
                if node.left:
                    level2.append(node.left)
                if node.right:
                    level2.append(node.right)
            level = level2
        return root
