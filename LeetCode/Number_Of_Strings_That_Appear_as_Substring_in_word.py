class Solution:
    def numOfStrings(self, patterns: list[str], word: str) -> int:
        count=0
        for i in range(0,len(patterns)):
            if patterns[i] in word:
                count+=1
        return count
