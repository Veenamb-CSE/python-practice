class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        result=0
        for i in words1:
            for j in words2:
                if i==j and words1.count(i)==1 and words2.count(j)==1 :
                    result+=1
        return result
        
