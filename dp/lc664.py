class Solution:
    def strangePrinter(self, s: str) -> int:
        n = len(s)
        int_max = 0x3f3f3f3f
        dp = [[int_max for _ in range(n)] for _ in range(n)]

        # print(dp)
        # @lru_cache(maxsize=2048)
        def dfs(i, j):
            if i < 0 or j >= n: return 0
            if i == j:
                return 1
            elif i > j:
                return 0
            elif i == j - 1:
                return 1 if (s[i] == s[j]) else 2
            if dp[i][j] != int_max: return dp[i][j]
            cnt = 0x3f3f3f3f
            for k in range(i + 1, j + 1):
                if s[k] == s[i]:
                    cnt = min(cnt, dfs(i, k - 1) + dfs(k + 1, j))
                else:
                    cnt = min(cnt, dfs(i, k - 1) + dfs(k, j))
            dp[i][j] = cnt
            return cnt

        return dfs(0, n - 1)
