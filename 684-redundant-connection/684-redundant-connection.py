class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        def check_cycle(n, adj_list, visited, parent):
            visited.add(n)
            for i in adj_list[n]:
                if i not in visited:
                    if check_cycle(i, adj_list, visited, n):
                        return True
                elif i!=parent:
                    return True
            return False
        def check_tree(edges_trial):
            adj_list = defaultdict(list)
            for i,j in edges_trial:
                adj_list[i].append(j)
                adj_list[j].append(i)
            visited = set()
            for i in range(1,len(adj_list)+1):
                if i not in visited:
                    result = check_cycle(i, adj_list, visited, -1)
                    if result:
                        return True
            return False
        for i in range(len(edges)-1,-1,-1):
            edges_trial = edges[:i]+edges[i+1:]
            if not check_tree(edges_trial):
                return edges[i]