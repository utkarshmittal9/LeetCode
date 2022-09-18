class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(row, col, visited):
            if row < 0 or col < 0 or row >= max_row or col >= max_col or grid[row][col]!="1":
                return 
            grid[row][col] = "#"
            dfs(row+1, col,visited)
            dfs(row-1, col,visited)
            dfs(row, col+1,visited)
            dfs(row, col-1,visited)
            
        if not grid:
            return 0
        island = 0
        visited = set()
        max_row = len(grid)
        max_col = len(grid[0])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1":
                    dfs(i,j, visited)
                    island+=1
        return island
        