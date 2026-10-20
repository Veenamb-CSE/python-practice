class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        letters = []

        for c in s:
            if c.isalpha():
                letters.append(c)

        letters.reverse()

        result = ""
        j = 0

        for c in s:
            if c.isalpha():
                result += letters[j]
                j += 1
            else:
                result += c

        return result

        
