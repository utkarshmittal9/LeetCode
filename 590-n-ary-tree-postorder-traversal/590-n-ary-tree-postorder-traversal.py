"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        self.post_list = []
        if not root:
            return 
        def _postorder(root):
            for i in root.children:
               _postorder(i) 
            self.post_list.append(root.val)
        _postorder(root)
        return self.post_list
            
        