class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if len(prerequisites) in [0,1]:
            return True
        adj_list = defaultdict(list)
        for i,j in prerequisites:
            adj_list[i].append(j)
        
        queue = []
        visited = set()
        
        def dfs(node, parent, dfs_vis):
            visited.add(node)
            dfs_vis.add(node)
            for i in adj_list[node]:
                if i not in visited:
                    if dfs(i, node, dfs_vis): return True
                elif i in dfs_vis:
                    return True
            dfs_vis.remove(node)
            return False
        
        for i in range(numCourses):
            dfs_vis = set()
            if i not in visited:
                if dfs(i, -1, dfs_vis): return False
        return True
        