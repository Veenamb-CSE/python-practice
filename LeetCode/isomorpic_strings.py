class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        str1 = {}
        str2 = {}

        for i in range(len(s)):

            if s[i] in str1:
                if str1[s[i]] != t[i]:
                    return False

            if t[i] in str2:
                if str2[t[i]] != s[i]:
                    return False

            str1[s[i]] = t[i]
            str2[t[i]] = s[i]

        return True
        
