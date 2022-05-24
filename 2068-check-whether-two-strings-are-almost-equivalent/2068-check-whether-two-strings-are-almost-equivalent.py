from collections import Counter
class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        word1 = Counter(word1)
        word2 = Counter(word2)
        for word,value in word1.items():
            if abs(value-word2.get(word,0))>3:
                return False
        for word,value in word2.items():
            if abs(value-word1.get(word,0))>3:
                return False
        return True
            
        