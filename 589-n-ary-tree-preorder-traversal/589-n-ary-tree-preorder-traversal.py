"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        self.post_list = []
        if not root:
            return 
        def _postorder(root):
            self.post_list.append(root.val)
            for i in root.children:
               _postorder(i) 
        _postorder(root)
        return self.post_list
        