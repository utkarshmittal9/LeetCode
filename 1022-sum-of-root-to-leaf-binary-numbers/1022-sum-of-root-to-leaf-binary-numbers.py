# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def _sum(root,res):
            if not root:
                return 0
            res = res*2 + root.val
            if not root.left and not root.right:
                return res
            return _sum(root.left,res) + _sum(root.right,res)
        return _sum(root,0)
                
        