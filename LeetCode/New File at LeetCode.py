class Solution:
    def trafficSignal(self, timer: int) -> str:
        if timer==0:
            return "Green"
        if timer==30:
            return "Orange"
        if timer>30 and timer<=90:
            return "Red"
        else:
            return "Invalid"
