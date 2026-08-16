class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        for i in range(0, len(s)):
            if s.count(s[i]) != t.count(s[i]):
                return False
