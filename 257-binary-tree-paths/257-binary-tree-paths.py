# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.paths = []
        def preorder(root, route):
            if root:
                preorder(root.left, route+"->"+str(root.val))
                
                preorder(root.right,route+"->"+str(root.val))
                if not root.left and not root.right:
                    self.paths.append(route+"->"+str(root.val))
        preorder(root,"")
        for i in range(len(self.paths)):
            self.paths[i] = self.paths[i][2:]
        return self.paths
            
                
        