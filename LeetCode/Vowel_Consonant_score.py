class Solution:
    def vowelConsonantScore(self, s: str) -> int:
        vowels = "aeiou"
        consonants = "bcdfghjklmnpqrstvwxyz"
        v=0
        c=0
        for i in range(len(s)):
            if s[i] in vowels:
                v+=1
            if s[i] in consonants:
                c+=1
        if v==0 or c==0:
            return 0
        else:
            return floor((v/c))
        
        
