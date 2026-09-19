class Solution:
    def clearDigits(self, s: str) -> str:
        stack=[]
        if s.isalpha():
            return s
        for i in s:
            if i.isalpha():
                stack.append(i)
            if i.isnumeric():
                stack.pop(-1)
        result = "".join(stack)
        return result
        
