class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        runningSum=[]
        for i in range(0,len(nums)):
            runningSum.append(sum(nums[:i+1]))
        return runningSum
        
