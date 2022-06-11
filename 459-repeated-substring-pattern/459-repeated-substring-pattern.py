class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if len(s) == 1:
            return False
        if len(set(s)) == 1:
            return True
        _len = len(s)
        def checkSubString(subString, s, _len):
            if _len%len(subString)!=0:
                return False
            rep = _len//len(subString)
            return s == subString * rep
            
        for i in range(1,_len//2):
            subString = s[:i+1]
            resp = checkSubString(subString, s, _len)
            if resp:
                return resp
        