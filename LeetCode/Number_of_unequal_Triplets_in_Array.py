class Solution:
    def unequalTriplets(self, nums: list[int]) -> int:
        count=0
        for i in range (0,len(nums)):
            for j in range (i+1,len(nums)):
                for k in range (j+1,len(nums)):
                    if nums[i] != nums[j] and nums[i] != nums[k]and nums[j] != nums[k]:
                        count+=1
        return count
        
