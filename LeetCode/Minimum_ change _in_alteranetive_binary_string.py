class Solution:
    def minOperations(self, s: str) -> int:

        count1 = 0   # Changes needed for 010101...
        count2 = 0   # Changes needed for 101010...

        for i in range(len(s)):

            if i % 2 == 0:
                # Even index
                if s[i] != '0':
                    count1 += 1

                if s[i] != '1':
                    count2 += 1

            else:
                # Odd index
                if s[i] != '1':
                    count1 += 1

                if s[i] != '0':
                    count2 += 1

        return min(count1, count2)
