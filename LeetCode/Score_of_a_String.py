class Solution:
    def scoreOfString(self, s: str) -> int:
        ascii_values = [ord(char) for char in s]
        count=0
        for i in range(1, len(ascii_values)):
            count+=abs(ascii_values[i]-ascii_values[i-1])
        return count
        
