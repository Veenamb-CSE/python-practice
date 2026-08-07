class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        matrix = []

        # Create m x n matrix filled with 0
        for i in range(m):
            row = []
            for j in range(n):
                row.append(0)
            matrix.append(row)

        # Process each [ri, ci]
        for ri, ci in indices:

            # Increase row ri
            for j in range(n):
                matrix[ri][j] += 1

            # Increase column ci
            for i in range(m):
                matrix[i][ci] += 1

        # Count odd numbers
        count = 0

        for i in range(m):
            for j in range(n):
                if matrix[i][j] % 2 != 0:
                    count += 1

        return count
