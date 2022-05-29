"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        self.list = []
        def maxd(root,level):
            if root:
                self.list.append(level)
                for child in root.children:
                    maxd(child, level+1)
        maxd(root, 1)
        return max(self.list)