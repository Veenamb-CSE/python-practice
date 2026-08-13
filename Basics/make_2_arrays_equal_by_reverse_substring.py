class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        for i in range(0, len(target)):
            tar = target.count(target[i])
            array = arr.count(target[i])

            if tar != array:
                return False
        return True
