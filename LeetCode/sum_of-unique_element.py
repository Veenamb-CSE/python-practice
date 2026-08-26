class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        list=[]
        for i in range(0,len(nums)):
            if nums.count(nums[i])==1:
                list.append(nums[i])
        return sum(list)
