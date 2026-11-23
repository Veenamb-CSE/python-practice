class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        list=[]
        for i in range (min(nums),max(nums)):
            if i not in nums:
                list.append(i)
        return list

        
