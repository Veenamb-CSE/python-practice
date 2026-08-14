class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        x=[]
        y=[]
        result=[]
        for i in range(0,len(nums)):
            if i>=n:
                y.append(nums[i])
            else:
                x.append(nums[i])
        for i in range(0,len(x)):
            result.append(x[i])
            result.append(y[i])
        return result
                
