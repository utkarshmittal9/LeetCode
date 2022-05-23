# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode, node = None) -> TreeNode:
        def inorder(root):
            if root:
                inorder(root.left)
                root.left = None
                self.dummy_node.right = root
                self.dummy_node = root
                inorder(root.right)
        self.dummy_node = TreeNode(0)
        i = self.dummy_node
        inorder(root)
        return i.right
        