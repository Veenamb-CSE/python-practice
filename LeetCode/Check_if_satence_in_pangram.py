class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alpahabet="abcdefghijklmnopqrstuvwxyz"
        for i in alpahabet:
            if i not in  sentence:
                return False
        
        return True
