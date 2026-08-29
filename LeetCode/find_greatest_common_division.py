class Solution:
    def findGCD(self, nums: List[int]) -> int:
        min_number = min(nums)
        max_number = max(nums)

        while min_number != 0:
            remainder = max_number % min_number
            max_number = min_number
            min_number = remainder

        return max_number
        
