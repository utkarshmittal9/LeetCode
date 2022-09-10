class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n==1:
            return 1
        dict_ = defaultdict(int)
        for n1,n2 in trust:
            dict_[n2] += 1
        assumed_judge = None
        for key, value in dict_.items():
            if value == n-1:
                assumed_judge = key
        if not assumed_judge:
            return -1
        for i,j in trust:
            if i==assumed_judge:
                return -1
            if i==assumed_judge and j==assumed_judge:
                return -1
        return assumed_judge
            