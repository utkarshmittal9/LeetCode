# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        self.list= {}
        def inorder(root):
            if root:
                inorder(root.left)
                self.list[root.val] = True
                inorder(root.right)
        inorder(root)
        for i in self.list.keys():
            if self.list.get(k-i) and k-i!=i:
                return True
        return False