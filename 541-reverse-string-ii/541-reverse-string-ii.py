class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        # if k <=1:
        #     return s
        # master_str = ""
        # if len(s) < k:
        #     return s[::-1]
        # if len(s) < 2*k and len(s) >= k:
        #     master_str = master_str + s[:k][::-1]+s[k:]
        #     return master_str
        # rem = len(s)%(2*k)
        # if rem:
        #     temp_str = s[:-rem]
        #     rem_str = s[-rem:]
        # else:
        #     temp_str = s
        # for i in range(0,len(temp_str),2*k):
        #     master_str = master_str + temp_str[i:i+k][::-1] + temp_str[i+k:i+2*k] 
        # if rem:
        #     if rem < k:
        #         master_str = master_str + rem_str[::-1]
        #     if rem < 2*k and rem >= k:
        #         master_str = master_str + rem_str[:k][::-1]+rem_str[k:]
        # return master_str
        s = list(s)
        for i in range(0,len(s),2*k):
            s[i:i+k] = s[i:i+k][::-1]
        return "".join(s)
        