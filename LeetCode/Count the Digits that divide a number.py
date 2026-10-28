class Solution:
    def countDigits(self, num: int) -> int:
        string=str(num)
        list=[]
        count=0
        for i in range(0,len(string)):
            list.append(string[i])
        for i in range(0,len(list)):
            if num%int(list[i])==0:
                count+=1
        return count
        
