class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        minimum_distance = 100000
        answer_index = -1
        for i in range(0,len(points)):
            if points[i][0]==x or points[i][1]==y:
                distance = abs(points[i][0]-x)+abs(points[i][1]-y)
                if distance < minimum_distance:
                    minimum_distance = distance
                    answer_index = i
        return answer_index
        
