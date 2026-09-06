class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        string=""
        i=0
        j=0
        while i<len(word1) or j<len(word2):
            if i<len(word1) and j<len(word2):
                string+=word1[i]
                i+=1
                string+=word2[j]
                j+=1
            else:
                if i<len(word1):
                    string+=word1[i]
                    i+=1
                else:
                    string+=word2[j]
                    j+=1
        return string

        
