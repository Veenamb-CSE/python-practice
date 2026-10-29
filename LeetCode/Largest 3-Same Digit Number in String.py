
class Solution:
    def largestGoodInteger(self, num: str) -> str:
        result = ""

        for i in range(len(num) - 2):
            if num[i] == num[i + 1] == num[i + 2]:
                good = num[i] * 3

                if good > result:
                    result = good

        return result
