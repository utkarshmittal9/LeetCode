class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        dict_ = defaultdict(list)
        for n1,n2 in edges:
            dict_[n1].append(n2)
            dict_[n2].append(n1)
        seen = set()
        print(dict_)
        def dfs(start, end, seen):
            if start == end:
                return True
            if start not in seen:
                seen.add(start)  
                for i in dict_[start]:
                        res = dfs(i, end, seen)
                        if res:
                            return True
        return dfs(source, destination, seen)
        