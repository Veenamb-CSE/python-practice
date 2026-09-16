class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        zeros = 0
        ones = 0
        ans = 0

        for i in range(len(s)):
            if s[i] == '0':
                if i > 0 and s[i - 1] == '1':
                    zeros = 0
                    ones = 0
                zeros += 1

            else:
                ones += 1
                ans = max(ans, 2 * min(zeros, ones))

        return ans
