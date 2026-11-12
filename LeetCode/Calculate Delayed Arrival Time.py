class Solution:
    def findDelayedArrivalTime(self, arrivalTime: int, delayedTime: int) -> int:
        result=arrivalTime+delayedTime
        if result==24:
            return 0
        if result>20:
            return result%24
        return result
        
