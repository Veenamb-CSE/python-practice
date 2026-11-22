class Solution:
    def countPrefixes(self, words: list[str], s: str) -> int:
        count = 0

        for i in range(0, len(words)):
            if s.startswith(words[i]):
                count += 1

        return count
