class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        list=[]
        for i in s:
            list.append(s.count(i))
        for i in range (1,len(list)):
            if list[0] !=list[i]:
                return False
        return True
