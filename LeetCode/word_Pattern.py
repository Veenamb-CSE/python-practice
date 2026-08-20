class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()

        if len(words) != len(pattern):
            return False

        dic1 = {}   # letter → word
        dic2 = {}   # word → letter

        for i in range(len(pattern)):
            letter = pattern[i]
            word = words[i]

            if letter in dic1:
                if dic1[letter] != word:
                    return False

            if word in dic2:
                if dic2[word] != letter:
                    return False

            dic1[letter] = word
            dic2[word] = letter

        return True
        
