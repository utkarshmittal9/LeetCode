"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        self.level = []
        def _maxDepth(root, level):
            if not root:
                self.level.append(0)
                return 
            if not root.children:
                self.level.append(level)
                return
            for child in root.children:
                _maxDepth(child, level+1)
        _maxDepth(root,1)
        if not self.level:
            return 0
        return max(self.level)