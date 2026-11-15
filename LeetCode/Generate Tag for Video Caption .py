
class Solution:
    def generateTag(self, caption: str) -> str:
        words = caption.split()
        
        result = "#"
        
        for i in range(len(words)):
            word = words[i].lower()
            
            if i == 0:
                result += word
            else:
                result += word.capitalize()
        
        result = "#" + ''.join(
            ch for ch in result[1:] if ch.isalpha()
        )
        
        return result[:100]
