# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def inorder(root, r_list):
            if root:
                inorder(root.left, r_list)
                if not root.left and not root.right:
                    r_list.append(root.val)
                inorder(root.right, r_list)
                return r_list
        
        return inorder(root1, []) == inorder(root2, [])
        
                    
        
        