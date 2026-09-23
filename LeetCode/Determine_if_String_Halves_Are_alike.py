class Solution:
    def halvesAreAlike(self, s: str) -> bool:

        vowel = ['a', 'e', 'i', 'o', 'u',
                 'A', 'E', 'I', 'O', 'U']

        a = []
        b = []

        for i in range(0, len(s)):
            if i < len(s) / 2:
                a.append(s[i])
            else:
                b.append(s[i])

        count_a = 0
        count_b = 0

        for i in a:
            if i in vowel:
                count_a += 1

        for i in b:
            if i in vowel:
                count_b += 1

        if count_a == count_b:
            return True

        return False
