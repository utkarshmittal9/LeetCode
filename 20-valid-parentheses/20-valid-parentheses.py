class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)<=1:
            return False
        _stack = list()
        compliment = {'{':'}','(':')','[':']'}
        for i in s:
            if i in compliment.keys():
                _stack = [i] + _stack
            elif i in ['}',')',']']:
                if not _stack or  i != compliment.get(_stack[0]):
                    return False
                _stack.pop(0)
        if not _stack:
            return True
        return False
