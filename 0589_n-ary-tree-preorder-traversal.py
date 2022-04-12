"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        stack = [[root,0]]
        ret = [root.val]
        while len(stack):
            node,index = stack[-1]
            if index == len(node.children):
                stack.pop()
            else:
                stack.append([node.children[index],0])
                ret.append(node.children[index].val)
                stack[-2][1] += 1
        return ret
