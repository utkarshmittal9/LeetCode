class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        num = list(number)
        _max = 0
        for i in range(len(num)):
            if num[i]==digit:
                temp = num[i]
                num[i] = ""
                temp_str = "".join(num)
                if int(temp_str)>_max:
                    _max = int(temp_str)
                num[i] = temp
        return str(_max)
        