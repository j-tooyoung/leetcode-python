# lc62
from math import comb


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return comb(m + n-2,m -1)

class Solution1:
    def uniquePaths(self, m: int, n: int) -> int:
        f = [[1] *n] + [[1] +[0] *(n-1) for _ in range(m-1)]
        print(f)
        for i in range(1,m):
            for j in range(1,n):
                f[i][j] = f[i - 1][j] + f[i][j-1]
        return f[m-1][n -1]



