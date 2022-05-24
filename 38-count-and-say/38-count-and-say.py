class Solution:
    def countAndSay(self, n: int) -> str:
        if n==1:
            return "1"
        def countandsay(n):
            str_n = str(n)
            new_str = ""
            i=0
            
            while i < len(str_n):
                count = 1
                for j in range(i+1,len(str_n)):
                    if str_n[j]!=str_n[i]:
                        break
                    i+=1
                    count+=1
                new_str = new_str + str(count)+str_n[i]
                i += 1
            return new_str
        return countandsay(self.countAndSay(n-1))
                
        