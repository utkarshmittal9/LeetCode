class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        hash_ = {}
        for pair in edges:
            for i in pair:
                if not hash_.get(i):
                    hash_[i] = 1
                else:
                    hash_[i] += 1
        for i in hash_.keys():
            if hash_[i] == len(edges):
                return i
        