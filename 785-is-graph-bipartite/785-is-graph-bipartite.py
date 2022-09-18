class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        col_track = [-1]*len(graph)
        def bfs(queue):
            while queue:
                node, col = queue.pop(0)
                for i in graph[node]:
                    if col_track[i]==-1:
                        if col==0:
                            col_track[i]=1
                            queue.append([i,1])
                        else:
                            col_track[i]=0
                            queue.append([i,0])
                    elif col_track[i]==col:
                        return False
            return True
        queue = []
        for i in range(len(graph)):
            if col_track[i]==-1:
                col_track[i]=0
                queue.append([i,0])
                if not bfs(queue):
                    return False
        return True
                
            
        