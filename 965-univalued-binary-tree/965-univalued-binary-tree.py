# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        self.track = set()
        self.flag = True
        def inorder(root):
            if root:
                inorder(root.left)
                self.track.add(root.val)
                if len(self.track)>1:
                    self.flag = False
                inorder(root.right)
        inorder(root)
        return self.flag