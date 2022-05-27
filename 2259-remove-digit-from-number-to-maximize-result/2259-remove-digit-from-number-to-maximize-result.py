class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        _max = 0
        # for i in range(len(num)):
        #     if num[i]==digit:
        #         temp = num[i]
        #         num[i] = ""
        #         temp_str = "".join(num)
        #         if int(temp_str)>_max:
        #             _max = int(temp_str)
        #         num[i] = temp
        # return str(_max)
        for i in range(len(number)):
            if number[i]==digit:
                temp = number[:i]+number[i+1:]
                if int(temp)>_max:
                    _max = int(temp)
        return str(_max)
                
        