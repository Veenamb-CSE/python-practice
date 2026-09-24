class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        k = 0
        repeated = ""

        while repeated + word in sequence:
            repeated += word
            k += 1

        return k
