class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        result=[]
        for i in range(0,len(words)):
            if x in words[i]:
                result.append(i)


        return result
                
