class Solution:
    def isValid(self, word: str) -> bool:
        vowels = "aeiouAEIOU"
        consonants = "bcdfghjklmnpqrstvwxyz"

        if len(word) < 3:
            return False

        val1 = False
        val2 = False

        for i in range(0, len(word)):

            if not word[i].isalnum():
                return False

            if word[i] in vowels:
                val1 = True

            if word[i].lower() in consonants:
                val2 = True

        if val1 and val2:
            return True
        else:
            return False
