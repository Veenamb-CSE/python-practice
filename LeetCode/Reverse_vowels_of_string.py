class Solution:
    def reverseVowels(self, s: str) -> str:
        str=[]
        for i in range(len(s)):
            str.append(s[i])
        vowels=["a","e","i","o","u","A","E","I","O","U"]
        dict=[]
        for i in range(0,len(s)):
            if s[i] in vowels:
                dict.append(s[i])
        dict.reverse()
        i=0
        j=0
        while i<len(s) and j<len(dict):
            if s[i] in vowels:
                str[i]=dict[j]
                j+=1
                i+=1
            else:
                i+=1
        string=""
        for i in range(0,len(str)):
            string+=str[i]
        return string
                
