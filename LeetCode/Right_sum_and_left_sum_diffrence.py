class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:

        left_sum = []
        right_sum = []

        # Left sum
        sum_value = 0

        for i in range(len(nums)):
            left_sum.append(sum_value)
            sum_value += nums[i]

        # Right sum
        value = 0

        for i in range(len(nums) - 1, -1, -1):
            right_sum.append(value)
            value += nums[i]

        right_sum.reverse()

        # Answer
        answer = []

        for i in range(len(nums)):
            answer.append(abs(left_sum[i] - right_sum[i]))

        return answer
