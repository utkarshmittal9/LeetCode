class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        count = 0
        _min_len = min(strs,key=len)
        for count in range(len(_min_len)):
            for i in range(1,len(strs)):
                if strs[i][count] != strs[i-1][count]:
                    return strs[i][:count]
        return _min_len
        