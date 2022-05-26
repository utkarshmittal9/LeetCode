class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        temp = []
        i = 0
        for i in range(len(s)):
            if s[i]!="#":
               temp.append(s[i])
            else:
                if temp:
                    temp.pop(-1)
        temp1 = []
        for i in range(len(t)):
            if t[i]!="#":
               temp1.append(t[i])
            else:
                if temp1:
                    temp1.pop(-1)
        return temp == temp1
                