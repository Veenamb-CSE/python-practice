class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()

        remove = len(arr) // 20

        arr = arr[remove:len(arr)-remove]

        return sum(arr) / len(arr) 
