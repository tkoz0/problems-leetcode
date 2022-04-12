"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        levels = []
        level = [root] if root else []
        while len(level):
            levels.append([r.val for r in level if r])
            level2 = []
            for r in level:
                if not r:
                    continue
                level2 += r.children
            level = level2
        return levels
