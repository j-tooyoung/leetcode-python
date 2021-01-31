from functools import lru_cache

# 动态规划 dfs
class Solution:
    def checkPartitioning(self, s: str) -> bool:
        @lru_cache(maxsize=2048)
        def dfs(start, cnt):
            if (cnt > 2):
                return False
            if (cnt == 2):
                return s[start:] == s[start:][::-1]
            for i in range(start, len(s)):
                if s[start:i + 1] == s[start:i + 1][::-1]:
                    if dfs(i+1, cnt + 1):
                        return True
            return False
        return dfs(0,0)