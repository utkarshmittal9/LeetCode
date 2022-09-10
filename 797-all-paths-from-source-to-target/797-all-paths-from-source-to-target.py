class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        graph_ = dict()
        for i, j in enumerate(graph):
            graph_[i] = j
        initial_node = 0
        final_node = len(graph) -1
        paths = []
        def find_paths(src, dest, path):
            if src == dest:
                paths.append(path)
            for i in graph_[src]:
                find_paths(i,dest,path + [i])
        find_paths(initial_node,final_node,[0])
        return paths