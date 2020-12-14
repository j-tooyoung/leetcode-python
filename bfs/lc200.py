from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        cnt = 0
        row, col = len(grid), len(grid[0]),

        def dfs(i: int, j: int, grid: List[List[str]]):
            if i < 0 or j < 0 or i >= row or j >= col:
                return
            if grid[i][j] == '0':
                grid[i][j] = '2'
                dfs(i + 1, j, grid)
                dfs(i - 1, j, grid)
                dfs(i, j + 1, grid)
                dfs(i, j - 1, grid)

        for i in range(0, row):
            for j in range(col):
                if grid[i][j] == '1':
                    dfs(i, j, grid)
                    cnt += 1
        return cnt


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row, col = len(grid), len(grid[0])

        def bfs(grid, i, j):
            q = [[i, j]]
            while q:
                [i, j] = q.pop()
                if 0 <= i < row and 0 <= j < col and grid[i][j] == '1':
                    grid[i][j] = '0'
                    q += [[i + 1, j], [i - 1, j], [i, j - 1], [i, j + 1]]

        count = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    bfs(grid, i, j)
                    count += 1
        return count