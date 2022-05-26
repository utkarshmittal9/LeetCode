class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        if not t:
            return False
        i = 0
        j = 0
        while i < len(s) and j < len(t):
            flag = False
            if s[i]!=t[j]:
                j = j+1
            elif s[i]==t[j]:
                i = i+1
                j = j+1
                flag = True
            if j == len(t) and (i <= (len(s) - 1) or not flag):
                return False
        return True
                        
            
        