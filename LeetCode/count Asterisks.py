class Solution:
    def countAsterisks(self, s: str) -> int:
        count = 0
        inside = False

        for i in s:
            if i == '|':
                inside = not inside
            elif i == '*' and inside == False:
                count += 1

        return count

        
