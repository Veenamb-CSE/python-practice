class Solution:
    def isPalindromic(self, s: str) -> bool:
        binary_8bit=""
        list=[]
        for i in range(0,len(s)):
            binary_8bit += f"{ord(s[i]):08b}"
        for i in range(0,len(binary_8bit)):
            list.append(int(binary_8bit[i]))
        if list[::]==list[::-1]:
            return True
        else:
            return False
        
