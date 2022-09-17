class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        final_list = []
        def masking(word):
            alphas = list(string.ascii_lowercase)
            maps = {}
            masked_word = ""
            for i in word:
                if not maps.get(i):
                    letter = alphas.pop(0)
                    maps[i] = letter
                    masked_word += letter
                else:
                    masked_word += maps.get(i)
            return masked_word
        masked_pattern = masking(pattern)
        for word in words:
            masked_word = masking(word)
            if masked_pattern == masked_word:
                final_list.append(word)
        return final_list
                
            
            
        
                
                