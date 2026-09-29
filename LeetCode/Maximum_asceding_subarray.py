class Solution:
    def maxAscendingSum(self, nums: list[int]) -> int:
        current = nums[0]
        maximum = nums[0]

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                current += nums[i]
            else:
                current = nums[i]

            maximum = max(maximum, current)

        return maximum
