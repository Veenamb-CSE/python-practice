class Solution:
    def reverseWords(self, s: str) -> str:
        list=s.split()
        str=""
        list=list[::-1]
        return " ".join(list)
        
