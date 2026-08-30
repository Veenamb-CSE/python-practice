class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitude = 0
        highest = 0

        for i in gain:
            altitude = altitude + i

            if altitude > highest:
                highest = altitude

        return highest
               

        
        
