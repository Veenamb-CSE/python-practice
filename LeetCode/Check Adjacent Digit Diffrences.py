class Solution:
    def isAdjacentDiffAtMostTwo(self, s: str) -> bool:
        list=[]
        for i in s:
            list.append(int(i))
        for i in range(1,len(list)):
            if abs(list[i-1]-list[i])>2:
                return False
        return True
        
