class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = {}

        # Count each character
        for i in range(len(s)):
            count[s[i]] = s.count(s[i])

        # Find the first character whose count is 1
        for i in range(len(s)):
            if count[s[i]] == 1:
                return i

        # No non-repeating character
        return -1
        
