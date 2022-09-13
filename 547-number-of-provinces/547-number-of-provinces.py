class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        len_ = len(isConnected)
        visited = set()
        province = 0
        def dfs(node):
            visited.add(node)
            for index, value in enumerate(isConnected[node]):
                if index!=node and value and index not in visited:
                    dfs(index)
                
        
        
        
        for i in range(len_):
                if  i not in visited:
                    dfs(i)
                    province += 1
                else:
                    continue
        return province
        
            
            
        
        