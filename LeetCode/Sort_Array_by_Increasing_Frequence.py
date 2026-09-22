class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:

        dict = {}

        # Find frequency of each number
        for i in range(0, len(nums)):
            dict[nums[i]] = nums.count(nums[i])

        # Get unique values
        values = list(dict.keys())

        # Sort by frequency increasing,
        # and value decreasing if frequency is same
        values.sort(key=lambda x: (dict[x], -x))

        # Create final answer
        result = []

        for i in values:
            for j in range(dict[i]):
                result.append(i)

        return result
