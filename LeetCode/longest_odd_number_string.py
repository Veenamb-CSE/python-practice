class Solution:
    def largestOddNumber(self, num: str) -> str:
        list = []
        str1 = ""

        for i in range(len(num)):
            list.append(int(num[i]))

        while len(list) > 0 and list[-1] % 2 == 0:
            list.pop()

        for i in range(len(list)):
            str1 += str(list[i])

        return str1
