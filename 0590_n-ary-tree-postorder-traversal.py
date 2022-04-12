"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        stack = [[root,0]]
        ret = []
        while len(stack):
            node,index = stack[-1]
            if index == len(node.children):
                stack.pop()
                ret.append(node.val)
            else:
                stack.append([node.children[index],0])
                stack[-2][1] += 1
        return ret
