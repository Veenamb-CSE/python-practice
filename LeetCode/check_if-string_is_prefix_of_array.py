class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        str=""
        for i in words:
            str+=i
            if str==s:
                return True
            if len(str)>len(s):
                return False
        return False
                
