from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix) - 1
        i = 0
        while i < (n + 1) // 2:
            j = i
            while j < n - i:
                temp = matrix[i][j]
                matrix[i][j] = matrix[n - j][i]
                matrix[n - j][i] = matrix[n - i][n - j]
                matrix[n - i][n - j] = matrix[j][n - i]
                matrix[j][n - i] = temp
                j += 1
            i += 1
