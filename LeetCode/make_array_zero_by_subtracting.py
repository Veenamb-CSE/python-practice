class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        count = 0

        while True:
            min_number = 0

            # Find smallest non-zero number
            for num in nums:
                if num != 0:
                    if min_number == 0 or num < min_number:
                        min_number = num

            # If all numbers are 0, stop
            if min_number == 0:
                break

            # Subtract minimum from every positive number
            for i in range(len(nums)):
                if nums[i] > 0:
                    nums[i] -= min_number

            count += 1

        return count
        
