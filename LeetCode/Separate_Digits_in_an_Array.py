class Solution:
    def separateDigits(self, nums: list[int]) -> list[int]:
        list=[str(nums[i]) for i in range(len(nums)) ]
        list1=[]
        for i in range (0,len(nums)):
            for j in range (0,len(list[i])):
                list1.append(list[i][j])
        list2=[int(list1[i]) for i in range(len(list1)) ]
        return list2
