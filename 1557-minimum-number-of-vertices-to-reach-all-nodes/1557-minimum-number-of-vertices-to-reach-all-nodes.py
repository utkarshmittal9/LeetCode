class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        adj_list = defaultdict(list)
        for i,j in edges:
            adj_list[j].append(i)
        small_vertices = []
        for i in range(n):
            if not adj_list.get(i):
                small_vertices.append(i)
        return small_vertices