class Solution:
    def getCommon(self, nums1: list[int], nums2: list[int]) -> int:
        list = []
        for i in range(0, len(nums1)):
            if nums1[i] in nums2:
                list.append(nums1[i])

        if len(list) == 0:
            return -1

        return min(list)
