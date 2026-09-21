class Solution:
    def residuePrefixes(self, s: str) -> int:
        chars = set()
        count = 0

        for i in range(len(s)):

            chars.add(s[i])

            if len(chars) == (i + 1) % 3:
                count += 1

        return count
        
