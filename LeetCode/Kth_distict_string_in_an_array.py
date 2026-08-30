class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        list=[]
        for i in range(0,len(arr)):
            if arr.count(arr[i])==1:
                list.append(arr[i])
        if len(list)>=k:
            return list[k-1]
        else:
            return ""
        
