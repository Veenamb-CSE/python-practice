class Solution:
    def maximumCount(self, nums: list[int]) -> int:
        count1=0
        count2=0
        for i in range(0,len(nums)):
            if nums[i]>0:
                count1+=1
            if nums[i]<0:
                count2+=1
        return max(count1,count2)
        
