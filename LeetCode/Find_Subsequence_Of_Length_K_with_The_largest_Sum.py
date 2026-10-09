class Solution:
    def maxSubsequence(self, nums: list[int], k: int) -> list[int]:
        arr = []
        
        for i in range(len(nums)):
            arr.append((nums[i], i))
        
        arr.sort(reverse=True)
        
        arr = arr[:k]
        arr.sort(key=lambda x: x[1])
        
        result = []
        for num, index in arr:
            result.append(num)
        
        return result
        
