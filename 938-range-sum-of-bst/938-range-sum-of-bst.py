# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.sum_list = []
        def inorder(root, low, high):
            if not root:
                return
            inorder(root.left,low,high)
            if root.val>=low and root.val<=high:
                self.sum_list.append(root.val)
            inorder(root.right,low,high)
        inorder(root,low,high)
        return sum(self.sum_list)