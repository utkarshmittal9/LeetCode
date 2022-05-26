class Solution:
    def checkRecord(self, s: str) -> bool:
        abs_count = 0
        for i in range(len(s)):
            if s[i]=="A":
                abs_count += 1
                if abs_count >=2:
                    return False
            elif s[i]=="L":
                if i+2<len(s):
                    if s[i+1]=="L" and s[i+2]=="L":
                        return False
        return True
        