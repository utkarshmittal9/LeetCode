# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        self.max_val = 0
        self.max_level = 0
        self.sum_ = 0
        def dfs(node, curr_level):
            if node:
                dfs(node.left, curr_level+1)
                dfs(node.right, curr_level+1)
                if not node.left and not node.right and self.max_level <= curr_level:
                    self.max_level = curr_level
                    self.max_val = node.val
        def dfs2(node,curr_level):
            if node:
                dfs2(node.left, curr_level+1)
                dfs2(node.right, curr_level+1)
                if not node.left and not node.right and self.max_level == curr_level:
                    self.sum_ += node.val
        dfs(root, 0)
        
        dfs2(root, 0)
        return self.sum_
        
                
                
        