class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # if len(strs)<=1 or len(set(strs))==1:
        #     return strs[0]
        # if "" in strs:
        #     return ""
        
        count = 0
        _min = min(strs, key = len)
        for i, ch in enumerate(_min):
            for j in strs:
                if j[i] != ch:
                    return _min[:i]
        return _min
        
        