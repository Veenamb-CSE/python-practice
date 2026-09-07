class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        value_sum = sum(nums)
        digit_sum = 0

        for num in nums:
            while num > 0:
                digit_sum += num % 10
                num = num // 10

        total = abs(value_sum - digit_sum)

        return total
