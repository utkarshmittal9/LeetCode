class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        vowels = []
        for i in range(len(s)):
            if s[i] in ['a','e','i','o','u','A','E','I','O','U']:
                vowels.append(s[i])
                s[i] = ""
        vowels = vowels[::-1]
        for i in range(len(s)):
            if not s[i]:
                s[i] = vowels.pop(0)
        return "".join(s)
            
        