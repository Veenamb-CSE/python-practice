class Solution:
    def addDigits(self, num: int) -> int:
            while num >= 10:
                count = 0
                for digit in str(num):
                    count += int(digit)
                num = count
            return num
        
