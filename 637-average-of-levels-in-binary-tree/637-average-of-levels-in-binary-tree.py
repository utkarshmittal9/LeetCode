# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        self.bfs_list = []
        def dfs(root, level):
            if root:
                self.bfs_list.append((root.val,level))
                dfs(root.left,level+1)
                dfs(root.right, level+1)
        dfs(root,0)
        sum_dict = {}
        for i,j in self.bfs_list:
            if sum_dict.get(j):
                sum_dict[j][0] += i
                sum_dict[j][1] += 1
            else:
                sum_dict[j] = [i,1]
        return [i/j for i,j in sum_dict.values()]
            
            
            
            
        