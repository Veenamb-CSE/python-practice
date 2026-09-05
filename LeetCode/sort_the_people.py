class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        for i in range(0, len(names)):
            for j in range(i + 1, len(heights)):
                if heights[i] < heights[j]:
                    temp = names[i]
                    names[i] = names[j]
                    names[j] = temp
                    temp = heights[i]
                    heights[i] = heights[j]
                    heights[j] = temp
        return names

        
