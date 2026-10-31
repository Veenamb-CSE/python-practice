class Solution:
    def isMiddleElementUnique(self, nums: list[int]) -> bool:
        if nums.count(nums[len(nums)//2])==1:
            return True
        else:
            return False
        
