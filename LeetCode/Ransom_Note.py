class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = {}

        for ch in magazine:
            if ch in count:
                count[ch] = count[ch] + 1
            else:
                count[ch] = 1

        for ch in ransomNote:

            if ch not in count:
                return False

            if count[ch] == 0:
                return False

            count[ch] = count[ch] - 1

        return True
        
