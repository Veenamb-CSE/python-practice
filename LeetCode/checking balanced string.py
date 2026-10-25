class Solution:
    def isBalanced(self, num: str) -> bool:
        list=[]
        even=0
        odd=0
        for i in range(0,len(num)):
            list.append(int(num[i]))
        for i in range(0,len(list)):
            if i%2==0:
                even+=list[i]
            else:
                odd+=list[i]
        if even==odd:
            return True
        else:
            return False
                
