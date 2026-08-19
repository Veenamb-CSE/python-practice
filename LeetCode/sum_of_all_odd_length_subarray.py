class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        ans=0
        for i in range(len(arr)):
            for j in range(i,len(arr)):
                length=j-i+1
                if length%2==1:
                    for k in range(i,j+1):
                        ans+=arr[k]
        return ans
        
