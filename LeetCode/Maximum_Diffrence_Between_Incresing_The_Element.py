class Solution:
    def maximumDifference(self, nums: list[int]) -> int:
            max_diff = -1

            for i in range(len(nums)):
                for j in range(i + 1, len(nums)):
                    if nums[i] < nums[j]:
                        count = nums[j] - nums[i]

                        if count > max_diff:
                            max_diff = count

            return max_diff
        
