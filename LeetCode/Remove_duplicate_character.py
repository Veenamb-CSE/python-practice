class Solution:
    def removeDuplicates(self, s: str) -> str:
        str=""
        for i in range (len(s)):
            if s.count(s[i])==1:
                str+=s[i]
        return str
