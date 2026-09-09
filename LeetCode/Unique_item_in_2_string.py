class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        list=s1.split()+s2.split()
        output=[]
        for i in list:
            if list.count(i)==1:
                output.append(i)
        
        return output
