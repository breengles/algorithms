from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        rows = []
        cols = []

        for i, row in enumerate(matrix):
            for j, val in enumerate(row):
                if val == 0:
                    rows.append(i)
                    cols.append(j)

        for i in rows:
            for j in range(n):
                matrix[i][j] = 0

        for j in cols:
            for i in range(m):
                matrix[i][j] = 0

