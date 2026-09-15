class Solution:
    def secondHighest(self, s: str) -> int:
        digits = []

        for i in s:
            if i.isnumeric():
                digits.append(int(i))

        digits = list(set(digits))
        digits.sort()

        if len(digits) < 2:
            return -1

        return digits[-2]
