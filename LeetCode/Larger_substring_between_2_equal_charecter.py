class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:

        max_length = -1

        for i in range(len(s)):
            for j in range(i + 1, len(s)):

                if s[i] == s[j]:
                    length = j - i - 1
                    max_length = max(max_length, length)

        return max_length
