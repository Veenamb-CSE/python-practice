class Solution:
    def smallestEqual(self, nums: list[int]) -> int:
        for i in range(0, len(nums)):
            if i%10==nums[i]:
                return i
        return -1
        
