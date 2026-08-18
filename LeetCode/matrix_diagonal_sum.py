class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        total = 0

        for i in range(n):

            total += mat[i][i]

            total += mat[i][n - 1 - i]

            if i == n // 2 and n % 2 == 1:
                total -= mat[i][i]

        return total
