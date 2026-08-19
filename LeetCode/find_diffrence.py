class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        str=""
        for i in range(0,len(t)):
            if s.count(t[i])!=t.count(t[i]):
                str=t[i]
        return str
