class Solution:
    def thousandSeparator(self, n: int) -> str:
        str1 = str(n)
        str3 = ""
        
        for i in range(len(str1)):
            if i > 0 and (len(str1) - i) % 3 == 0:
                str3 += "."
            str3 += str1[i]
        
        return str3
