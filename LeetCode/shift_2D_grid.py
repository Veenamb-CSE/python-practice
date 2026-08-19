class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)          # Number of rows
        n = len(grid[0])       # Number of columns
        total = m * n          # Total number of elements

        k = k % total          # Reduce unnecessary shifts

        # Create an empty result grid
        result = [[0] * n for _ in range(m)]

        # Place each element in its new position
        for i in range(m):
            for j in range(n):
                index = i * n + j
                newIndex = (index + k) % total

                newRow = newIndex // n
                newCol = newIndex % n

                result[newRow][newCol] = grid[i][j]

        return result
        
