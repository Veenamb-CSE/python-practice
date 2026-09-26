class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        number = 0
        for ch in firstWord:
            digit = ord(ch) - ord('a')
            number = number * 10 + digit
        number1 = 0
        for ch in secondWord:
            digit = ord(ch) - ord('a')
            number1 = number1 * 10 + digit 
        number2 = 0
        for ch in targetWord:
            digit = ord(ch) - ord('a')
            number2 = number2 * 10 + digit 
        if number+number1==number2:
            return True
        else:
            return False
        
