class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        s=s.split()
        str=[]
        for i in range(0,len(s)):
            if i>=k:
                break
            else:
                str.append(s[i])
        return " ".join(str)

        
