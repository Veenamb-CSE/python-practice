class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        missing = 0
        num = 1
        i = 0

        while missing < k:

            if i < len(arr) and arr[i] == num:
                i += 1
            else:
                missing += 1

                if missing == k:
                    return num

            num += 1
        
