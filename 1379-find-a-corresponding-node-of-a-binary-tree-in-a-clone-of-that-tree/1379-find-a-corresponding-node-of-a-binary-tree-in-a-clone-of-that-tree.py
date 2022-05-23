# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        self.result = None
        def inorder(self,original, cloned, target):
            if not original:
                return 
            inorder(self,original.left, cloned.left, target)
            if original == target:
                self.result = cloned
            inorder(self,original.right, cloned.right, target)
        inorder(self,original, cloned, target)
        return self.result
            
                