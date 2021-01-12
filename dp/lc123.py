import functools
from typing import List


# 123.  买卖股票的最佳时机  III
class Solution:
    # 超时
    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)
        ans = 0

        # 0为不持有， 1为持有
        @functools.lru_cache(maxsize=1024)
        def dfs(index, k, state):
            if k == 0 or index >= length:
                return 0
            a, b, c = 0, 0, 0
            if state == 1:
                b = dfs(index + 1, k - 1, 0) + prices[index]
            else:
                c = dfs(index + 1, k, 1) - prices[index]
            a = dfs(index + 1, k, state)
            return max(a, b, c)

        return dfs(0, 2, 0)

    # dict优化 勉强过
    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)
        d = dict()
        # 0为不持有， 1为持有
        # @functools.lru_cache(maxsize=1024)
        def dfs(index, k, state):
            if (index, k, state) in d:
                return d[index, k, state]
            if k == 0 or index >= length:
                return 0
            a, b, c = 0, 0, 0
            if state == 1:
                b = dfs(index + 1, k - 1, 0) + prices[index]
            else:
                c = dfs(index + 1, k, 1) - prices[index]
            a = dfs(index + 1, k, state)
            d[index, k, state] = max(a, b, c)
            return d[index, k, state]

        return dfs(0, 2, 0)

    # dp数组
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if not prices:
            return 0
        dp = [[[float('-inf')] * 2 for _ in range(3)] for _ in range(n)]
        print(dp)
        # 初始条件
        for i in range(n):
            dp[i][0][0] = 0
        dp[i][0][1] = -prices[0]
        for i in range(n):
            # 当k为0的时候，第一个方程不适用，因为会出现-1
            dp[i][0][1] = max(dp[i-1][0][1], -prices[i])
            for k in range(1,3):
                dp[i][k][0] = max(dp[i-1][k][0],dp[i-1][k - 1][1] +prices[i])
                dp[i][k][1] = max(dp[i-1][k][1],dp[i-1][k][0] -prices[i])
        res = 0
        for i in range(3):
            res = max(res, dp[n-1][i][0])
        return res

        # dp数组优化
        def maxProfit(self, prices: List[int]) -> int:
            n = len(prices)
            if not prices:
                return 0
            dp = [[[float('-inf')] * 2 for _ in range(3)] for _ in range(n)]
            print(dp)
            # 初始条件
            for i in range(n):
                dp[i][0][0] = 0
            dp[i][0][1] = -prices[0]
            for i in range(n):
                # 当k为0的时候，第一个方程不适用，因为会出现-1
                dp[i][0][1] = max(dp[i - 1][0][1], -prices[i])
                for k in range(1, 3):
                    dp[i][k][0] = max(dp[i - 1][k][0], dp[i - 1][k - 1][1] + prices[i])
                    dp[i][k][1] = max(dp[i - 1][k][1], dp[i - 1][k][0] - prices[i])
            res = 0
            for i in range(3):
                res = max(res, dp[n - 1][i][0])
            return res

