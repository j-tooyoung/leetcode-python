from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        row = len(matrix)
        if row == 0:
            return 0
        col = len(matrix[0])
        # print(row,col)
        left = [[0 for i in range(col)] for j in range(row)]
        # print(left)
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == '1':
                    left[i][j] = 1 if j == 0 else left[i][j - 1] + 1
        res = 0
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == '1':
                    width = left[i][j]
                    area = width
                    for k in range(i - 1, -1, -1):
                        width = min(width, left[k][j])
                        area = max(area, width * (i - k + 1))
                    res = max(res, area)
        return res
