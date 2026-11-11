class Solution:
    def checkGoodInteger(self, n: int) -> bool:
        string=str(n)
        list=[]
        list1=[]
        for i in range(0,len(string)):
            list.append(int(string[i]))
            list1.append((int(string[i]))**2)
        sum1=sum(list)
        sum2=sum(list1)
        result=sum2-sum1
        if result>= 50:
            return True
        else:
            return False
        
